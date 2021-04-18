import { createEffect, createStore } from 'effector';

import { api } from '../../utils/api';
// export const fetchTableFx = createEffect(() => api.get('/api/reports/saved-reports/'));
// export const $table = createStore([]).on(fetchTableFx.doneData, (_, { data }) => data);
export const fetchReportsFx = createEffect(() => api.get('/reports/saved-reports/'));
export const $reports = createStore([]).on(fetchReportsFx.doneData, (_, { data }) => data);
