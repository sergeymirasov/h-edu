import { attach, createEffect } from 'effector';

import { api } from '../../../utils/api';
import { $reportId } from '../model';

export const saveReportNameFx = createEffect(({ id, data }) =>
  api.patch(`/reports/saved-reports/${id}/`, data),
);
export const reportSaved = attach({
  effect: saveReportNameFx,
  source: $reportId,
  mapParams: (data, id) => {
    return {
      id,
      data,
    };
  },
});
