import FormBuilder from 'antd-form-builder';
import { Button, Space, Steps } from 'antd';
import { useCallback, useEffect, useState } from 'react';
import { useStore } from 'effector-react';
import { Helmet } from 'react-helmet';
import { useHistory } from 'react-router-dom';

import { PageContent } from '../../components/page-content';
import { StyledPage, StyledForm, StyledFormContent } from './styles';
import { createMeta } from './helpers';
import { useNotifyError, useNotifySuccess } from '../../hooks/use-notification';
import {
  $dataSourceOptions,
  $slitsOptions,
  fetchDataSourceFx,
  fetchSlitsFx,
  fetchFiltersFx,
  fetchColumnsFx,
  $filtersFields,
  sendReportFx,
  fetchColumnSetsFx,
  $columns,
  $columnSets,
  reportSent,
} from './model';

export const Report = () => {
  const [form] = StyledForm.useForm();
  const [currentStep, setCurrentStep] = useState(0);
  const [activeKey, setActiveKey] = useState([0]);
  const history = useHistory();
  const forceUpdate = FormBuilder.useForceUpdate();
  const slitsOptions = useStore($slitsOptions);
  const dataSourceOptions = useStore($dataSourceOptions);
  const columns = useStore($columns);
  const columnSets = useStore($columnSets);
  const filtersFields = useStore($filtersFields);
  const { meta } = createMeta({
    form,
    dataSourceOptions,
    slitsOptions,
    columns,
    columnSets,
    filtersFields,
    activeKey,
    setActiveKey,
  });
  const stepsLength = meta.steps.length;
  const isLastSteep = currentStep === stepsLength - 1;

  const onValuesChange = useCallback(() => {
    const { data_source_name, slit_name } = form.getFieldsValue();

    if (data_source_name && slit_name) {
      fetchColumnsFx({ data_source_name, slit_name });
      fetchColumnSetsFx({ data_source_name, slit_name });
      fetchFiltersFx({ data_source_name, slit_name });
    }

    forceUpdate();
  }, [forceUpdate, form]);

  const onFinish = useCallback(() => {
    reportSent(form.getFieldsValue(true));
  }, [form]);

  const onCancel = useCallback(() => {
    setCurrentStep(0);
    form.resetFields();
  }, [form]);

  const handleNext = useCallback(() => {
    form.validateFields().then(() => {
      setCurrentStep(currentStep + 1);
    });
  }, [currentStep, form]);

  const handleBack = useCallback(() => {
    form.validateFields().then(() => {
      setCurrentStep(currentStep - 1);
    });
  }, [currentStep, form]);

  useNotifySuccess(sendReportFx, 'Отчет успешно создан');
  useNotifyError(sendReportFx, 'Произошла ошибка при отправке отчета');

  useEffect(() => {
    fetchSlitsFx();
    fetchDataSourceFx();
  }, []);

  useEffect(() => {
    const subscription = reportSent.finally.watch(({ status }) => {
      if (status === 'done') {
        onCancel();
        history.push('/report/preview');
      }
    });

    return () => subscription.unsubscribe();
  }, [history, onCancel]);

  return (
    <StyledPage>
      <Helmet>
        <title>Создание отчета | PROF</title>
      </Helmet>

      <PageContent title="Новый отчет">
        <StyledForm
          layout="horizontal"
          form={form}
          onValuesChange={onValuesChange}
          onFinish={onFinish}
        >
          <Steps current={currentStep}>
            {meta.steps.map(({ title }) => (
              <Steps.Step key={title} title={title} />
            ))}
          </Steps>

          <StyledFormContent>
            <FormBuilder
              viewMode={currentStep === stepsLength}
              form={form}
              meta={meta.steps[currentStep].formMeta}
            />
          </StyledFormContent>

          <StyledForm.Item className="form-footer" style={{ textAlign: 'right' }}>
            {currentStep > 0 ? (
              <Button onClick={handleBack} style={{ float: 'left' }}>
                Назад
              </Button>
            ) : null}

            <Space>
              <Button onClick={onCancel}>Отмена</Button>
              <Button type="primary" onClick={isLastSteep ? () => form.submit() : handleNext}>
                {isLastSteep ? 'Сформировать отчет' : 'Продолжить'}
              </Button>
            </Space>
          </StyledForm.Item>
        </StyledForm>
      </PageContent>
    </StyledPage>
  );
};
