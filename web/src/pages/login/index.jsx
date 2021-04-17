import { Input, Button, Checkbox, Form } from 'antd';
import { useStore } from 'effector-react';
import { useEffect } from 'react';
import { useHistory } from 'react-router-dom';

import { StyledPage, StyledContainer, StyledTitle } from './styles';
import { userLogged } from '../../models/auth';
import { $token } from '../../models/user';

const layout = {
  labelCol: {
    span: 4,
  },
  wrapperCol: {
    span: 20,
  },
};

const tailLayout = {
  wrapperCol: {
    offset: 4,
    span: 20,
  },
};

export const Login = () => {
  const history = useHistory();
  const token = useStore($token);

  useEffect(() => {
    if (token) {
      history.push('/personal/application');
    }
  }, [history, token]);

  const onFinish = ({ username, password }) => {
    userLogged({
      username,
      password,
    });
  };

  const onFinishFailed = (info) => {
    console.warn(info);
  };

  return (
    <StyledPage>
      <StyledContainer>
        <StyledTitle>Авторизация</StyledTitle>

        <Form
          {...layout}
          name="login"
          initialValues={{
            remember: true,
          }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
        >
          <Form.Item
            label="Логин"
            name="username"
            rules={[
              {
                required: true,
                message: 'Пожалуйста, введите имя!',
              },
            ]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Пароль"
            name="password"
            rules={[
              {
                required: true,
                message: 'Пожалуйста, введите пароль!',
              },
            ]}
          >
            <Input.Password />
          </Form.Item>

          <Form.Item {...tailLayout} name="remember" valuePropName="checked">
            <Checkbox>Запомнить меня</Checkbox>
          </Form.Item>

          <Form.Item {...tailLayout}>
            <Button type="primary" htmlType="submit">
              Войти
            </Button>
          </Form.Item>
        </Form>
      </StyledContainer>
    </StyledPage>
  );
};
