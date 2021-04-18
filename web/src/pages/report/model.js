import { createEffect, createStore, attach, createEvent } from 'effector';
import { persist } from 'effector-storage/local/fp';

import { api } from '../../utils/api';
import { RangeInput } from './helpers';

export const fetchDataSourceFx = createEffect(() => api.get('/reports/data-sources/'));
export const $dataSource = createStore([]).on(fetchDataSourceFx.doneData, (_, { data }) => data);
export const $dataSourceOptions = $dataSource.map((items) =>
  items.map(({ name, label }) => ({ value: name, label })),
);

export const fetchSlitsFx = createEffect(() => api.get('/reports/slits/'));
export const $slits = createStore([]).on(fetchSlitsFx.doneData, (_, { data }) => data);
export const $slitsOptions = $slits.map((items) =>
  items.map(({ name, label }) => ({ value: name, label })),
);

export const fetchColumnsFx = createEffect((params) => api.get('/reports/columns/', { params }));
export const $columns = createStore([]).on(fetchColumnsFx.doneData, (_, { data }) => data);
export const $columnsCheckboxes = $columns.map((items) =>
  items.map(({ key, label }) => ({ value: key, label })),
);

export const fetchColumnSetsFx = createEffect((params) =>
  api.get('/reports/columnsets/', { params }),
);
export const $columnSets = createStore([]).on(fetchColumnSetsFx.doneData, (_, { data }) => data);

export const fetchFiltersFx = createEffect((params) => api.get('/reports/filters/', { params }));
export const $filters = createStore([]).on(fetchFiltersFx.doneData, (_, { data }) => data);
export const $filtersFields = $filters.map((items) =>
  items.map((item) => {
    if (item.type === 'number') {
      return {
        key: `filters_data.${item.key}`,
        label: item.label,
        widget: RangeInput,
        initialValue: { from: null, to: null },
      };
    }

    if (item.type === 'choices') {
      return {
        key: `filters_data.${item.key}`,
        label: item.label,
        widget: 'select',
        widgetProps: {
          mode: 'multiple',
        },
        options: item.choices,
      };
    }
  }),
);

export const sendReportFx = createEffect((data) => api.post('/reports/saved-reports/', data));
export const reportSent = attach({
  effect: sendReportFx,
  mapParams: ({ data_source_name, slit_name, columns_data, filters_data }) => {
    return {
      data_source_name,
      slit_name,
      columns_data: Object.entries(columns_data)
        .map(([, value]) => value)
        .flat(),
      filters_data,
    };
  },
});
export const resetReportId = createEvent();
export const $reportId = createStore(null)
  .on(sendReportFx.doneData, (_, { data }) => data.id)
  .reset(resetReportId)
  .thru(persist({ key: 'report-id' }));
