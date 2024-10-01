# Используем базовый образ Python 3.11
FROM python:3.11-slim

ARG DATABASE_NAME
ARG DATABASE_USER
ARG DATABASE_PASSWORD
ARG DATABASE_HOST
ARG DATABASE_PORT

ENV DATABASE_NAME=${DATABASE_NAME}
ENV DATABASE_USER=${DATABASE_USER}
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}
ENV DATABASE_HOST = ${DATABASE_HOST}
ENV DATABASE_PORT = ${DATABASE_PORT}

# Устанавливаем необходимые зависимости, включая python3 и curl
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean

# Устанавливаем Poetry
RUN pip install poetry

RUN poetry config virtualenvs.create false

# Задаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта для установки зависимостей
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости через Poetry
RUN poetry install --no-root --no-interaction --no-ansi

# Копируем остальные файлы проекта
COPY . /app

# Открываем порт для Django
EXPOSE 8000

# Задаем переменные окружения для Django и PostgreSQL
ENV DJANGO_SETTINGS_MODULE=deposit.settings
ENV DATABASE_URL=postgresql://${DATABASE_USER}:${DATABASE_PASSWORD}@${DATABASE_HOST}:${DATABASE_PORT}/${DATABASE_NAME}

# Выполняем миграции и запускаем сервер Django

CMD ["poetry", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000"]
