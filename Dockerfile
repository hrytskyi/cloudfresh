# Вказуємо базовий образ
FROM python:3.12-slim

# Встановлюємо залежності для системи
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

#Робимо апгрейд піп
RUN pip install --upgrade pip

# Встановлюємо залежності
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade flask werkzeug

# Копіюємо файли застосунку
COPY . /app
WORKDIR /app

# Встановлюємо змінні середовища
ARG MONGODB_URI
ARG SECRET_KEY
ARG DB_NAME

ENV MONGODB_URI=$MONGODB_URI
ENV SECRET_KEY=$SECRET_KEY
ENV DB_NAME=$DB_NAME
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Відкриваємо порт
EXPOSE 5000

# Запускаємо Flask-застосунок
CMD ["flask", "run"]
