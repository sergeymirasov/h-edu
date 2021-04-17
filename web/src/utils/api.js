import axios from 'axios';

import { $token } from '../models/user';

export const api = axios.create({
  baseURL: 'http://prof.laitprojects.site/api/',
});

api.interceptors.request.use((config) => {
  const token = $token.getState();

  if (token) {
    config.headers.Authorization = `Token ${token}`;
  } else {
    config.headers.Authorization = null;
  }

  return config;
});
