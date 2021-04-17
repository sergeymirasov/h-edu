import moment from 'moment';
import { Input, Form, Row, Col, Select, DatePicker, Button } from 'antd';
import { Fragment } from 'react';
import { MinusCircleOutlined, PlusOutlined } from '@ant-design/icons';
import 'moment/locale/ru';

import { AccentWrapper, StyledPage } from './styles';
import { Container } from '../../../components/container';
import { ContentTitle } from '../../../components/content-title';
import { FieldWrapper } from '../../../components/field-wrapper';

const initialValues = {};

export const Application = () => {
  const [form] = Form.useForm();

  const onFinish = (values) => {
    console.log(values);
    // console.log(moment(values.birth_date).format('YYYY-MM-DD'));
  };

  const onFinishFailed = (info) => {
    console.warn(info);
  };

  return (
    <StyledPage>
      <Container>
        <ContentTitle size="large">Новое заявление о приеме</ContentTitle>

        <Form
          name="application"
          form={form}
          initialValues={initialValues}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
        >
          {/* ================================================================================== */}
          {/* Персональные данные */}
          {/* ================================================================================== */}
          <ContentTitle size="medium">Персональные данные</ContentTitle>

          <Row gutter={[32, 0]}>
            <Col span={6}>
              <FieldWrapper label="Фамилия">
                <Form.Item name="first_name">
                  <Input placeholder="Иванов" />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={6}>
              <FieldWrapper label="Имя">
                <Form.Item name="last_name">
                  <Input placeholder="Сергей" />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={6}>
              <FieldWrapper label="Отчество">
                <Form.Item name="middle_name">
                  <Input placeholder="Владимирович" />
                </Form.Item>
              </FieldWrapper>
            </Col>
          </Row>
          <Row gutter={[32, 0]}>
            <Col span={6}>
              <FieldWrapper label="Дата рождения">
                <Form.Item name="birth_date">
                  <DatePicker
                    placeholder="01.02.1995"
                    style={{ width: '100%' }}
                    format="DD.MM.YYYY"
                  />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={12}>
              <FieldWrapper label="Место рождения">
                <Form.Item name="birth_place">
                  <Input placeholder="Место рождения" />
                </Form.Item>
              </FieldWrapper>
            </Col>
          </Row>
          <Row gutter={[32, 0]}>
            <Col span={6}>
              <FieldWrapper label="Гражданство">
                <Form.Item name="citizenship">
                  <Select placeholder="Российская Федерация">
                    <Select.Option value="ru">Российская Федерация</Select.Option>
                    <Select.Option value="en">Великобритания</Select.Option>
                  </Select>
                </Form.Item>
              </FieldWrapper>
            </Col>
          </Row>
          {/* ================================================================================== */}
          {/* Документ, удостоверяющий личность */}
          {/* ================================================================================== */}
          <AccentWrapper>
            <ContentTitle size="small">Документ, удостоверяющий личность</ContentTitle>

            <Form.List name="passport">
              {() => (
                <Fragment>
                  <Row gutter={[32, 0]}>
                    <Col span={6}>
                      <FieldWrapper label="Документ">
                        <Form.Item name="type">
                          <Select>
                            <Select.Option value="passport">Паспорт</Select.Option>
                          </Select>
                        </Form.Item>
                      </FieldWrapper>
                    </Col>
                    <Col span={6}>
                      <FieldWrapper label="Серия">
                        <Form.Item name="series">
                          <Input placeholder="2214" />
                        </Form.Item>
                      </FieldWrapper>
                    </Col>
                    <Col span={6}>
                      <FieldWrapper label="Номер">
                        <Form.Item name="num">
                          <Input placeholder="325673" />
                        </Form.Item>
                      </FieldWrapper>
                    </Col>
                  </Row>
                  <Row gutter={[32, 0]}>
                    <Col span={6}>
                      <FieldWrapper label="Когда выдан рождения">
                        <Form.Item name="issued_at">
                          <DatePicker
                            placeholder="01.02.1995"
                            format="DD.MM.YYYY"
                            style={{ width: '100%' }}
                          />
                        </Form.Item>
                      </FieldWrapper>
                    </Col>
                    <Col span={12}>
                      <FieldWrapper label="Кем выдан">
                        <Form.Item name="issued_by">
                          <Input placeholder="УМВД России по Томской области" />
                        </Form.Item>
                      </FieldWrapper>
                    </Col>
                  </Row>
                </Fragment>
              )}
            </Form.List>
          </AccentWrapper>
          {/* ================================================================================== */}
          {/* Адрес проживания */}
          {/* ================================================================================== */}
          <ContentTitle size="small">Адрес проживания</ContentTitle>

          <Row gutter={[32, 0]}>
            <Col span={6}>
              <FieldWrapper label="Страна">
                <Form.Item name="">
                  <Input placeholder="Российская Федерация" />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={6}>
              <FieldWrapper label="Область">
                <Form.Item name="">
                  <Input placeholder="Томская" />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={6}>
              <FieldWrapper label="Район">
                <Form.Item name="">
                  <Input placeholder="Томский" />
                </Form.Item>
              </FieldWrapper>
            </Col>
          </Row>
          <Row gutter={[32, 0]}>
            <Col span={6}>
              <FieldWrapper label="Улица">
                <Form.Item name="">
                  <Input placeholder="Советская" />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={4}>
              <FieldWrapper label="Дом">
                <Form.Item name="">
                  <Input placeholder="31а" />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={4}>
              <FieldWrapper label="Квартира">
                <Form.Item name="">
                  <Input placeholder="144" />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={4}>
              <FieldWrapper label="Индекс">
                <Form.Item name="">
                  <Input placeholder="661255" />
                </Form.Item>
              </FieldWrapper>
            </Col>
          </Row>
          {/* ================================================================================== */}
          {/* Контактные данные */}
          {/* ================================================================================== */}
          <ContentTitle size="small">Контактные данные</ContentTitle>

          <Row gutter={[32, 0]}>
            <Col span={6}>
              <FieldWrapper label="Личный телефон">
                <Form.Item name="">
                  <Input placeholder="+7___-__-__" />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={6}>
              <FieldWrapper label="Домашний (при наличии)">
                <Form.Item name="">
                  <Input placeholder="" />
                </Form.Item>
              </FieldWrapper>
            </Col>
            <Col span={6}>
              <FieldWrapper label="Электронная почта">
                <Form.Item name="">
                  <Input placeholder="example@mail.ru" />
                </Form.Item>
              </FieldWrapper>
            </Col>
          </Row>
          {/* ================================================================================== */}
          {/* Обучение */}
          {/* ================================================================================== */}
          <ContentTitle size="medium">Обучение</ContentTitle>

          <FieldWrapper label="Основная профессия">
            <Form.List name="profession">
              {(fields, { add, remove }) => (
                <Fragment>
                  {fields.map(({ key, name, fieldKey, ...restField }) => (
                    <div key={key} className="dynamic-field">
                      <Form.Item
                        {...restField}
                        name={[name, 'type']}
                        fieldKey={[fieldKey, 'type']}
                        style={{
                          marginBottom: 16,
                        }}
                      >
                        <Select placeholder="Выберите из списка">
                          <Select.Option value="A">Профессия A</Select.Option>
                          <Select.Option value="B">Профессия B</Select.Option>
                        </Select>
                      </Form.Item>
                      <MinusCircleOutlined
                        className="dynamic-delete-button"
                        onClick={() => remove(name)}
                      />
                    </div>
                  ))}

                  <Form.Item style={{ marginTop: 16 }}>
                    <Button
                      type="primary"
                      onClick={() => add()}
                      style={{ display: 'flex', alignItems: 'center' }}
                      icon={<PlusOutlined />}
                    >
                      Добавить профессию
                    </Button>
                  </Form.Item>
                </Fragment>
              )}
            </Form.List>
          </FieldWrapper>
          {/* ================================================================================== */}
          {/* Образование */}
          {/* ================================================================================== */}
          <Form.Item>
            <Button type="primary" htmlType="submit" size="large">
              Сохранить
            </Button>
          </Form.Item>
        </Form>
      </Container>
    </StyledPage>
  );
};
