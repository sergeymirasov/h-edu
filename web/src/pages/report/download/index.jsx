import { Button, Input, Space, Form } from 'antd';
import { CheckCircleOutlined } from '@ant-design/icons';
import { Fragment, useCallback, useEffect, useMemo } from 'react';
import { useStore } from 'effector-react';
import { useHistory, useLocation } from 'react-router-dom';
import { Helmet } from 'react-helmet';

import { PageContent } from '../../../components/page-content';
import { LinkButton } from '../../../components/link-button';
import { StyledPage } from './styles';
import { baseURL } from '../../../utils/api';
import { $reportId } from '../model';
import { reportSaved } from './model';

export const Download = () => {
  const [form] = Form.useForm();
  const history = useHistory();
  const location = useLocation();
  const splittedPathname = location.pathname.split('/');
  const lastPathnameItem = splittedPathname[splittedPathname.length - 1];
  const locationReportId = useMemo(() => (!isNaN(lastPathnameItem) ? lastPathnameItem : null), [
    lastPathnameItem,
  ]);
  const reportId = useStore($reportId);

  const onFinish = useCallback(() => {
    const values = form.getFieldsValue(true);

    reportSaved(values);

    if (values.name) {
      window.open(`${baseURL}reports/saved-reports/${reportId}/export/`);
    }
  }, [form, reportId]);

  useEffect(() => {
    if (!reportId) {
      history.push('/report');
    }
  }, [history, reportId]);

  return (
    <StyledPage>
      <Helmet>
        <title>Загрузка отчета | PROF</title>
      </Helmet>

      <PageContent title="Новый отчет">
        <div className="info-block">
          <Space direction="vertical" align="center" size={24}>
            <CheckCircleOutlined style={{ fontSize: '80px', color: '#6bc51b' }} />

            <h2>Отчет cформирован</h2>

            {!locationReportId ? (
              <Form form={form} initialValues={{ name: null }} onFinish={onFinish}>
                <Form.Item
                  name="name"
                  rules={[
                    {
                      required: true,
                      message: 'Пожалуйста, введите название отчета!',
                    },
                  ]}
                >
                  <Input size="large" placeholder="Название отчета" style={{ width: 340 }} />
                </Form.Item>
              </Form>
            ) : null}

            <Space>
              {locationReportId ? (
                <Button
                  href={`${baseURL}reports/saved-reports/${locationReportId}/export/`}
                  type="primary"
                  size="large"
                  target="_blank"
                >
                  Скачать
                </Button>
              ) : (
                <Fragment>
                  <LinkButton size="large" to="/report/preview">
                    Вернуться к предпросмотру
                  </LinkButton>

                  <Button onClick={() => form.submit()} type="primary" size="large">
                    Скачать и сохранить
                  </Button>
                </Fragment>
              )}
            </Space>

            <LinkButton type="link" to="/report">
              Создать новый отчет
            </LinkButton>
          </Space>
        </div>
      </PageContent>
    </StyledPage>
  );
};
