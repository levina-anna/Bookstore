FROM python:3.11.5

RUN pip install --upgrade pip
RUN apt update && apt install nano

ENV DJANGO_SETTINGS_MODULE=AdminPanel.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Bookstore

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /Bookstore

WORKDIR /Bookstore/AdminPanel

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD python3 manage.py migrate && gunicorn AdminPanel.wsgi:application --bind 0.0.0.0:8000
