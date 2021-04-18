import { notification } from 'antd';
import { useEffect } from 'react';

export const useNotifySuccess = (fx, message, description) =>
  useEffect(() => {
    const subscription = fx.finally.watch(({ status }) => {
      if (status === 'done') {
        notification.success({
          message,
          description,
          duration: 3,
          top: 80,
        });
      }
    });

    return () => subscription.unsubscribe();
  }, [description, fx, message]);

export const useNotifyError = (fx, message, description) =>
  useEffect(() => {
    const subscription = fx.finally.watch(({ status, error }) => {
      if (status === 'fail') {
        console.log(error);

        notification.error({
          message,
          description,
          duration: 3,
          top: 80,
        });
      }
    });

    return () => subscription.unsubscribe();
  }, [description, fx, message]);
