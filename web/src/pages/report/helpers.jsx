import FormBuilder from 'antd-form-builder';
import { Input, Collapse } from 'antd';

export const RangeInput = ({ value, onChange }) => {
  return value ? (
    <Input.Group compact>
      <Input
        value={value.from}
        onChange={(v) => onChange({ from: v.target.value || null, to: value.to || null })}
        style={{ width: '25%' }}
      />
      <Input
        value={value.to}
        onChange={(v) => onChange({ to: v.target.value || null, from: value.from || null })}
        style={{ width: '25%' }}
      />
    </Input.Group>
  ) : null;
};

export const createCollapsibleCheckedList = ({
  form,
  columns,
  columnSets,
  activeKey,
  setActiveKey,
}) => {
  return (
    <Collapse activeKey={activeKey} onChange={setActiveKey}>
      {columnSets.map(({ label, items }, index) => (
        <Collapse.Panel header={label} key={index}>
          <FormBuilder
            form={form}
            meta={{
              key: `columns_data.${index}`,
              widget: 'checkbox-group',
              options: items.map(({ column_key }) => ({
                value: column_key,
                label: columns.find(({ key }) => key === column_key).label,
              })),
              // noStyle: true,
            }}
          />
        </Collapse.Panel>
      ))}
    </Collapse>
  );
};

export const createMeta = ({
  form,
  dataSourceOptions,
  slitsOptions,
  columns,
  columnSets,
  filtersFields,
  activeKey,
  setActiveKey,
}) => {
  const meta = {
    steps: [
      {
        title: 'Данные и разрез',
        formMeta: {
          columns: 1,
          fields: [
            {
              key: 'data_source_name',
              label: 'Источник данных',
              placeholder: 'Выберите из списка',
              widget: 'select',
              options: dataSourceOptions,
              required: true,
            },
            {
              key: 'slit_name',
              label: 'Разрез',
              placeholder: 'Выберите из списка',
              widget: 'select',
              options: slitsOptions,
              required: true,
            },
          ],
        },
      },
      {
        title: 'Поля',
        formMeta: {
          columns: 1,
          fields: [
            {
              widget: 'input.search',
              key: 'columns_search',
              placeholder: 'Введите название фильтра',
            },
            {
              key: 'columns_data_last_item',
              readOnly: true,
              viewWidget: () =>
                createCollapsibleCheckedList({
                  form,
                  columns,
                  columnSets,
                  activeKey,
                  setActiveKey,
                }),
              required: true,
              // rules: [{ type: 'columns_data', message: 'Пожалуйста, выберите минимум 1 элемент' }],
            },
          ],
        },
      },
      {
        title: 'Фильтры',
        formMeta: {
          columns: 1,
          fields: [
            {
              widget: 'input.search',
              key: 'filters_search',
              placeholder: 'Введите название фильтра',
            },
            ...filtersFields,
          ],
        },
      },
    ],
  };

  return { meta };
};
