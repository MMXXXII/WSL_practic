# Python Environment Setup

Учебный проект по настройке окружения для разработки на Python.

## Структура проекта
- app/ — исходный код программы
- examples/ — скриншоты и примеры работы
- requirements.txt — зависимости проекта

## Запуск API

1. Активировать виртуальное окружение:
source venv/bin/activate
2. Убедиться, что PostgreSQL запущен:
sudo service postgresql start

3. Запустить сервер:
uvicorn app.main:app --reload

4. Открыть в браузере:
- http://127.0.0.1:8000/health — проверка работоспособности
- http://127.0.0.1:8000/docs — интерактивная документация Swagger

## Эндпоинты

- GET /categories/ — список категорий
- POST /categories/ — создать категорию
- GET /categories/{id} — получить категорию
- PUT /categories/{id} — обновить категорию
- DELETE /categories/{id} — удалить категорию
- GET /books/ — список книг (поддерживает ?category_id=)
- POST /books/ — создать книгу
- GET /books/{id} — получить книгу
- PUT /books/{id} — обновить книгу
- DELETE /books/{id} — удалить книгу

