import { Route, Switch, useRouteMatch } from 'react-router-dom';

import { Application as ApplicationPage } from '../pages/personal/application';

export const Personal = () => {
  const { url } = useRouteMatch();

  return (
    <Switch>
      <Route path={`${url}/application`} component={ApplicationPage} />
    </Switch>
  );
};
