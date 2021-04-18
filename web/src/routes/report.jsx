import { Route, Switch } from 'react-router-dom';

import { Report as ReportPage } from '../pages/report';
import { Download as DownloadPage } from '../pages/report/download';
import { Preview as PreviewPage } from '../pages/report/preview';

export const Report = () => {
  return (
    <Switch>
      <Route path="/report/preview" component={PreviewPage} />
      <Route path="/report/download" component={DownloadPage} />
      <Route path="/report" component={ReportPage} />
    </Switch>
  );
};
