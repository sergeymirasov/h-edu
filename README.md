<p align="center">
    <h1 align="center">H Edu</h1>
    </p>

<h4>Реализованная функциональность</h4>
<ul>
    <li>Функционал 1;</li>
    <li>Функционал 2;</li>
    <li>Функционал 3;</li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Киллерфича-1;</li>
 <li>Киллерфича-2;</li>
 <li>Киллерфича-3;</li>  
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
  <li>HTML, CSS, JavaScript, React</li>
  <li>Python, Django</li>
  <li>LESS, styled-components</li>
  <li>Webpack, Babel</li>
  <li>Git</li>
</ul>
<h4>Демо</h4>
<p>Демо сервиса доступно по адресу: http://prof.laitprojects.site/auth/login </p>
<p>Реквизиты тестового пользователя: логин: <b>admin</b>, пароль: <b>qwe123098</b></p>
<p>Админка сервиса доступно по адресу: http://prof.laitprojects.site/admin/login/?next=/admin/ </p>
<p>Реквизиты тестового пользователя: логин: <b>admin</b>, пароль: <b>qwe123098</b></p>




СРЕДА ЗАПУСКА
------------
1) развертывание сервиса происходит с помощью docker-контейнеров. Для удобства создания используется docker-compose

УСТАНОВКА
------------
### Установка docker и docker-compose

Выполните 
~~~
sudo apt update
sudo apt upgrade
sudo apt install docker python3-pip
sudo pip3 install docker-compose
git clone https://github.com/sergeymirasov/h-edu
cd h-edu
docker-compose build
docker-compose up
~~~

### Выполнение миграций

Для заполнения базы данных системной информацией выполните в корневой папке сервиса: 
~~~
docker-compose run django python manage.py migrate
~~~

### Создание админ пользователя

~~~
docker-compose run django python manage.py createsuperuser
~~~

РАЗРАБОТЧИКИ

<h4>Мирасов Сергей (Frontend) https://t.me/newbornfrontender</h4>
<h4>Гусев Анатолий (Backend) https://t.me/laitenrayn</h4>


