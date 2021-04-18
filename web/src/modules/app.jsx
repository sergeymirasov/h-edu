import locale from 'antd/lib/locale/ru_RU';
import FormBuilder from 'antd-form-builder';
import { ConfigProvider } from 'antd';
import { ThemeProvider } from 'styled-components';
import { DatePicker, Input } from 'antd';
import 'antd/dist/antd.css';

import { Routes } from '../routes';
import { colors } from '../theme/colors';

FormBuilder.defineWidget('input.search', Input.Search);
FormBuilder.defineWidget('date-picker.range-picker', DatePicker.RangePicker);

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
