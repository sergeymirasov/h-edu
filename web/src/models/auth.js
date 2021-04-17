import { createEffect, forward, createEvent } from 'effector';

import { api } from '../utils/api';
import { userInfoChanged } from './user';

export const userLogged = createEvent();
export const userLoginFx = createEffect((data) => api.post('/auth/token/login/', data));

export const userLogouted = createEvent();
export const userLogoutFx = createEffect(() => api.post('/auth/token/logout/'));

forward({
  from: userLogged,
  to: userLoginFx,
});

userLoginFx.doneData.watch(({ data }) => userInfoChanged({ token: data.auth_token }));
