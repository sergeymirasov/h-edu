import { useStore } from 'effector-react';
import { Helmet } from 'react-helmet';

import { PageContent } from '../../components/page-content';
import { StyledPage, StyledTable } from './styles';
import { $reports, fetchReportsFx } from './model';
import { useEffect } from 'react';

export const Reports = () => {
  const reports = useStore($reports);
  console.log(reports);

  useEffect(() => {
    fetchReportsFx();
  }, []);

  return (
    <StyledPage>
      <Helmet>
        <title>Мои отчеты | PROF</title>
      </Helmet>

      <PageContent title="Мои отчеты">
        <StyledTable bordered dataSource={[]} columns={[]} />
      </PageContent>
    </StyledPage>
  );
};
