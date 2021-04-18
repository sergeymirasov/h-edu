import { Route, Switch, Redirect } from 'react-router-dom';

import { Report as ReportPage } from '../pages/personal/report';

export const Personal = () => {
  return (
    <Switch>
      <Route path="/personal/report" component={ReportPage} />

      <Redirect exact from="/personal" to="/personal/report" />
    </Switch>
  );
};
