import { attach, createEffect, createStore } from 'effector';

import { api } from '../../../utils/api';
import { $reportId } from '../model';

export const fetchTableFx = createEffect((id) =>
  api.get(`/reports/saved-reports/${id}/json-preview/`),
);
export const tableReceived = attach({
  effect: fetchTableFx,
  source: $reportId,
});
export const $table = createStore([]).on(fetchTableFx.doneData, (_, { data }) => data);
