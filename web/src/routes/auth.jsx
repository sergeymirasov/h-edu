import { Route, Switch, Redirect, useRouteMatch } from 'react-router-dom';

import { Login as LoginPage } from '../pages/login';

export const Auth = () => {
  const { url } = useRouteMatch();

  return (
    <Switch>
      <Route path={`${url}/login`} component={LoginPage} />

      <Redirect exact from={url} to={`${url}/login`} />
    </Switch>
  );
};
