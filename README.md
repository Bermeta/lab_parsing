# lab_parsing
Для запуска проекта нужно будет:
 - Создать репозиторий.
 - Склонить c командой: git clone https://github.com/Bermeta/lab_paring.git
 - Создать виртуальное окружение: python3 -m venv venv
 - Активировать окружение: . venv/bin/activate
 - Скачать нужные библиотеки из файла requirements.txt
 - Создать базу данных 
 - Создать .env поместив туда  свои данные связанные с базой данных: 
USERNAME=имя пользователя postgres, 
PASSWORD=пароль  пользователя (работает без конфига, так как с main не запускался.)
HOST=host, DB_NAME=имя базы данных.
 - команда для запуска parsing.py: python3 parsing.py
 - команда для запуска  main.py: python3 main.py
 - команда для экспорта в SQL: pg_dump -U postgres -h localhost lab_parsing > apart_data.sql