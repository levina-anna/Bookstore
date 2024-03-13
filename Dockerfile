# Используем образ Python
FROM python:3.11.5

# обновляю пакеты, устанавливаю нано
RUN pip install --upgrade pip
RUN apt update && apt install nano

# Устанавливаем переменную окружения для Django
ENV DJANGO_SETTINGS_MODULE=AdminPanel.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /Bookstore

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости Django
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /Bookstore

# Переход
WORKDIR /Bookstore/AdminPanel

# Собираем статические файлы Django
RUN python3 manage.py collectstatic --noinput

# Открываем порт, на котором будет работать приложение Django
EXPOSE 8000

# Запускаем Gunicorn при старте контейнера
CMD python3 manage.py migrate && gunicorn AdminPanel.wsgi:application --bind 0.0.0.0:8000
