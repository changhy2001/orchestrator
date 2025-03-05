FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=myproject.settings

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

RUN python manage.py collectstatic --noinput

CMD ["daphne", "myproject.asgi:application", "--bind", "0.0.0.0", "--port", "8000"]