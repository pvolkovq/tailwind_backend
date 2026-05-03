# tailwind-backend

## Описание

**---** **WIP** **---**

Tailwind — это веб-приложение на базе Django для управления портфолио художников. Проект позволяет пользователям создавать портфолио, загружать свои работы (изображения), подписываться на портфолио других пользователей, оставлять комментарии к работам и управлять видимостью контента.

## Технологии

- **Backend**: Django 6.0, Django REST Framework
- **База данных**: PostgreSQL
- **Хранение файлов**: Локальное (в разработке) или S3 (в продакшене, через django-storages)
- **Контейнеризация**: Docker, Docker Compose
- **Управление зависимостями**: uv
- **Дополнительно**: Pillow (для обработки изображений), Markdown, Debug Toolbar

## Установка

### Предварительные требования

- Python >= 3.14
- Docker и Docker Compose
- uv (для управления зависимостями)

### Шаги установки

1. **Клонируйте репозиторий**:
   ```bash
   git clone <repository-url>
   cd tailwind
   ```

2. **Создайте виртуальное окружение и установите зависимости**:
   ```bash
   uv install
   ```

3. **Создайте файл `.env` в корне проекта** с необходимыми переменными окружения:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DB_ENGINE=django.db.backends.postgresql
   POSTGRES_DB=your-db-name
   POSTGRES_USER=your-db-user
   POSTGRES_PASSWORD=your-db-password
   DB_HOST=localhost
   DB_PORT=5432
   ```

   Для генерации SECRET_KEY можно использовать:
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(50))"
   ```

4. **Запустите базу данных и приложение с помощью Docker Compose**:
   ```bash
   docker-compose up --build
   ```

   Это запустит PostgreSQL и Django-сервер на порту 8000.

## Использование

### Запуск сервера

```bash
make serv
```

Сервер будет доступен по адресу: http://localhost:8000

### Админка

Доступ к Django admin: http://localhost:8000/admin/

### API

Приложение предоставляет REST API для взаимодействия с данными.

#### Основные эндпоинты

- `GET/POST /api/v1/portfolios/` — Список портфолио / Создание портфолио
- `GET/POST /api/v1/artworks/` — Список работ / Создание работы

API использует Django REST Framework с разрешениями `DjangoModelPermissionsOrAnonReadOnly` (чтение для всех, запись только для аутентифицированных пользователей с соответствующими правами).

#### Примеры запросов

Получить список портфолио:
```bash
curl http://localhost:8000/api/v1/portfolios/
```

Создать работу (требуется аутентификация):
```bash
curl -X POST http://localhost:8000/api/v1/artworks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Моя работа", "image": "path/to/image.jpg", "user": 1, "portfolio": 1}'
```

