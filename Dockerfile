# Вказуємо базовий образ
FROM python:3.8-slim

# Встановлюємо залежності для системи
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо pipenv та додаткові пакети
RUN pip install --upgrade pip

# Встановлюємо залежності
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копіюємо файли застосунку
COPY . /app
WORKDIR /app

# Встановлюємо змінні середовища
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Відкриваємо порт
EXPOSE 5000

# Запускаємо Flask-застосунок
CMD ["flask", "run"]
