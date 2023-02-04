# TodoList

Задача:

Необходимо создать Django приложение Todo List. У приложение должно быть 5 Api
методов:

1. Создание записи /api/record/create - POST ***[DONE]***
2. Чтение записи /api/record/get?uuid={string} - GET ***[DONE]***
3. Список записей /api/records/all - GET ***[DONE]***
4. Список записей на указанные даты /api/records/list?start={DD.MM.YY}&end={DD.MM.YY} - GET ***[DONE]***
5. Удаление записи /api/record/delete?uuid={string} - DELETE ***[DONE]***

# Install
### Запуск произодится через Docker
- Склонировать репозиторий
    ```git clone https://github.com/kekoslav42/TodoList.git```
- Перейти в папку backend 
    ```cd TodoList/backend```
- Переименовать `example.env` в `.env`
- Заполнить этот файл если нужно
- выполнить команду `docker-compose up --build`

После запуска докер контейнера будет доступна документация апишки `http://localhost:8000/api/docs/` или `http://localhost:8000/api/redoc/`
