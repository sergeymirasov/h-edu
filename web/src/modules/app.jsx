import locale from 'antd/lib/locale/ru_RU';
import { ConfigProvider } from 'antd';
import { ThemeProvider } from 'styled-components';
import 'antd/dist/antd.css';

import { Routes } from '../routes';
import { colors } from '../theme/colors';

const theme = {
  colors,
};

export const App = () => {
  return (
    <ConfigProvider locale={locale}>
      <ThemeProvider theme={theme}>
        <Routes />
      </ThemeProvider>
    </ConfigProvider>
  );
};
