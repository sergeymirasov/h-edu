import React from 'react';
import { Route, Redirect } from 'react-router-dom';

export const Guard = ({ routes: Routes, isAuth, ...rest }) => (
  <Route
    {...rest}
    render={(props) => (isAuth === true ? <Routes {...props} /> : <Redirect to="/auth/login" />)}
  />
);
