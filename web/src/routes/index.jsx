import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import { Layout } from 'antd';
import { useStore } from 'effector-react';

import { Auth as AuthRoute } from './auth';
import { Personal as PersonalRoute } from './personal';
import { Guard } from './components/guard';
import { $token } from '../models/user';

export const Routes = () => {
  const token = useStore($token);

  return (
    <Router>
      <Layout>
        <Layout.Content>
          <Switch>
            {/* <Guard
              isAuth={token}
              path="/personal"
              routes={() => (
                <Switch>
                  <Route path="/personal" component={PersonalRoute} />
                </Switch>
              )}
            /> */}

            <Route path="/personal" component={PersonalRoute} />
            <Route path="/auth" component={AuthRoute} />

            <Redirect exact from="/" to="/auth" />
          </Switch>
        </Layout.Content>
      </Layout>
    </Router>
  );
};
