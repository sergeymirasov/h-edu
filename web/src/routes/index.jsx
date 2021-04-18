import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import { Layout } from 'antd';

import { Header } from '../components/header';
import { Report as ReportRoute } from './report';
import { Reports as ReportsPage } from '../pages/reports';

export const Routes = () => {
  return (
    <Router>
      <Layout>
        <Header />

        <Layout.Content>
          <Switch>
            <Route path="/report" component={ReportRoute} />
            <Route path="/reports" exact component={ReportsPage} />

            <Redirect exact from="/" to="/report" />
          </Switch>
        </Layout.Content>
      </Layout>
    </Router>
  );
};
