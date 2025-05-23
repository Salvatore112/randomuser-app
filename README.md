# Тестовое задание
[![CI](https://github.com/Salvatore112/randomuser-app/actions/workflows/ci.yml/badge.svg)](https://github.com/Salvatore112/randomuser-app/actions/workflows/ci.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Приложение для взаимодействия с внешним API: https://randomuser.me/api/

## Обоснование выбора технологий  

**Веб-фреймворк: Flask**  
Выбран за свою минималистичность и гибкость. Как микрофреймворк, Flask идеально подходит для небольших приложений, предоставляя только необходимую функциональность через расширения.

**База данных: SQLite**  
Оптимальный выбор для данного проекта благодаря:  
- Отсутствию необходимости в отдельном сервере БД  
- Хранению всей БД в одном файле (`users.db`)  
- Достаточной производительности для операций CRUD  
- Полной совместимости с SQLAlchemy ORM  

**Дополнительные технологии:**  
- `requests` для получения данных с randomuser.me API  
- `Bootstrap 5` для быстрого создания интерфейса  

Такое сочетание технологий обеспечивает баланс между:  
1. Простотой разработки и развертывания  
2. Гибкостью архитектуры  
3. Достаточной производительностью  
4. Возможностью масштабирования при необходимости

Кроме всего вышеперечисленного, выбор был обусловлен наличием опыта работы с данным стеком.

## Установка и запуск

```bash
https://github.com/Salvatore112/randomuser-app.git
cd console-chat.git
sudo docker-compose build
```
### Запуск сервиса
```bash
sudo docker-compose up web
```
### Запуск тестов
```bash
sudo docker-compose up test
```

