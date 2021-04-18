import axios from 'axios';

import { $token } from '../models/user';

export const baseURL = 'http://prof.laitprojects.site/api/';
export const api = axios.create({
  baseURL,
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
