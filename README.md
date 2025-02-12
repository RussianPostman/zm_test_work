Для тестового запуска необходимо:

1. Создать и заполнить файл с переменными окружения:

```
DATABASE_HOST=postgres
DATABASE_NAME=my_db
DATABASE_PASS=root
DATABASE_PORT=5432
DATABASE_USER=root
```

2. Запустить проект командой

```
docker-compose up -d --build
```

3. Работа с API

Документация со списком эндпоинтов будет доступна по "http://localhost:8004/docs"

Быстро проверить при запуске можно через такой запрос: 

Список существующих задач (при старте есть уже 4)
- GET: http://0.0.0.0:8004/tasks/list/
