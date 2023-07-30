## Сервис получения информации о лучших клиентах


### Описание
1. Принимает из POST-запроса .csv файлы, содержащие истории сделок.
2. Сохраняет данные о сделках в базу.
3. При GET-запросе возвращает из 5 клиентов, потративших наибольшую сумму за весь период. По каждому клиенту возвращает список из названий камней, которые купили как минимум двое из лучших клиентов, и данный клиент является одним из этих покупателей.


### Структура .csv-файла для POST-запроса
Строка с заголовком не обрабатывается. Строки должны иметь вид: `customer,item,total,quantity,date`
- customer - логин покупателя
- item - наименование товара
- total - сумма сделки
- quantity - количество товара, шт
- date - дата и время регистрации сделки


### Шаблон заполнения .env-файла, создаётся в общей директории (используйте свои параметры)

SECRET_KEY=secret                         _(Секретный ключ для работы с проектом)_

DB_ENGINE=django.db.backends.postgresql   _(Движок для работы с БД)_

DB_NAME=postgres                          _(Название БД)_

POSTGRES_USER=postgres                    _(Имя пользователя БД)_

POSTGRES_PASSWORD=postgres                _(Пароль для доступа к БД)_

DB_HOST=db                                _(Адрес БД (контейнер docker))_

DB_PORT=5432                              _(Порт для подключения к БД)_


### Запуск проекта

1. Создайте в общей директории .env-файл, заполните его согласно образцу в .env.example.

2. Добавьте адрес вашего хоста в список `ALLOWED_HOSTS` в файле `settings.py` или используйте `127.0.0.1` для запуска локально.

3. Установите Docker и docker-compose, подходящие для вашей операционной системы (следуйте инструкциям по установке консольной или десктопной версий на официальных сайтах). Запустите Docker.

4. Перейдите в общую директорию и запустите проект командой:
`docker-compose up`


### API
Спецификация API-запросов и список эндпоинтов доступны по адресам (проект должен быть запущен):  
http://адрес_хоста:8000/swagger/  
http://адрес_хоста:8000/redoc/  


### Версия языка Python
`3.11.3`


### Стек технологий
`Django` `Django REST Framework` `PostgreSQL` `Gunicorn` `Docker` `docker-compose`


### Author
_Max Stepanov_  
_GitHub: NewZealandMax_
