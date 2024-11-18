# Базовый образ
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get clean

# Копируем и устанавливаем Python-зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код проекта
COPY . .

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Собираем статику на этапе сборки (опционально, можно сделать на уровне CI/CD)
RUN python manage.py collectstatic --noinput

# Выполняем миграции базы данных (можно оставить на уровне CI/CD)
RUN python manage.py migrate --noinput

# Запускаем приложение через Gunicorn
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
