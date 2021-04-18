import { useStore } from 'effector-react';
import { useEffect, useMemo } from 'react';
import { Helmet } from 'react-helmet';
import { useHistory, useLocation } from 'react-router-dom';

import { PageContent } from '../../../components/page-content';
import { StyledPage, StyledButtons, StyledTable } from './styles';
import { $table, tableReceived, fetchTableFx } from './model';
import { $reportId } from '../model';
import { LinkButton } from '../../../components/link-button';

export const Preview = () => {
  const history = useHistory();
  const location = useLocation();
  const splittedPathname = location.pathname.split('/');
  const lastPathnameItem = splittedPathname[splittedPathname.length - 1];
  const locationReportId = useMemo(() => (!isNaN(lastPathnameItem) ? lastPathnameItem : null), [
    lastPathnameItem,
  ]);
  const table = useStore($table);
  const reportId = useStore($reportId);
  const isLoading = useStore(fetchTableFx.pending);

  useEffect(() => {
    if (!reportId) {
      history.push('/report');
    } else {
      if (locationReportId) {
        fetchTableFx(locationReportId);
      } else {
        tableReceived();
      }
    }
  }, [history, locationReportId, reportId]);

  return (
    <StyledPage>
      <Helmet>
        <title>Предпросмотр отчета | PROF</title>
      </Helmet>

      <PageContent title="Новый отчет">
        <StyledButtons>
          <LinkButton to="/report">Создать новый отчет</LinkButton>
          <LinkButton to="/report/download" type="primary">
            Скачать отчет
          </LinkButton>
        </StyledButtons>

        <StyledTable
          bordered
          dataSource={table?.dataSource}
          columns={table?.columns}
          loading={isLoading}
          // title={() => 'Заголовок таблицы'}
          // footer={() => 'Описание таблицы или полезная информация'}
        />
      </PageContent>
    </StyledPage>
  );
};
