import { createEffect, forward, createEvent, createStore } from 'effector';
import { persist } from 'effector-storage/local/fp';

import { api } from '../utils/api';

const initialUserState = {
  email: null,
  id: null,
  username: null,
  token: null,
};

export const userInfoReceived = createEvent();
export const userInfoChanged = createEvent();
export const fetchUserInfoFx = createEffect(() => api.get('/auth/users/me/'));
export const $user = createStore(initialUserState)
  .on(fetchUserInfoFx.doneData, (state, { data }) => ({ ...state, ...data }))
  .on(userInfoChanged, (state, { token }) => ({ ...state, token }))
  .thru(persist({ key: 'user' }));

forward({ from: userInfoReceived, to: fetchUserInfoFx });
forward({ from: userInfoChanged, to: userInfoReceived });

export const $token = $user.map(({ token }) => token);
