# Telegram Bot for Pizzeria

Данный проект позволяет запустить telegram-бота, который будет показывать меню из базы данных. Базу можно редактировать по [адресу](http://localhost:5000). В составе проекта есть скрипт, который создаёт базу и выполняет первичную загрузку данных.

## Подготовка

- зарегистрировать нового бота для разработки и получить токен [@BotFather](https://telegram.me/botfather)
- записать токен в файл envvars, а также адрес БД, логин/пароль для администратора

## Первичная настройка
Для объявления всех переменных выполнить в терминале:
```bash
source envvars
```
Установить все необходимые зависимости:
```
pip3 install -r requirements.txt
```
Создать БД:
```
python3 create_db.py
```

## Запуск
Для запуска выполняем в терминале:
```
python3 server.py &
python3 bot.py &
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
