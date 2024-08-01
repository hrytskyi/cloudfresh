import requests
import json
import csv
import matplotlib.pyplot as plt

# API URL та ключ
api_url = "http://data.fixer.io/api/latest"
access_key = "YOUR_ACCESS_KEY"

# Отримання даних з API
response = requests.get(f"{api_url}?access_key={access_key}")
data = response.json()

# Збереження даних у JSON файл
with open('exchange_rates.json', 'w') as json_file:
    json.dump(data, json_file)

# Обробка даних та збереження у CSV файл
rates = data['rates']
with open('exchange_rates.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Currency', 'Rate'])
    for currency, rate in rates.items():
        writer.writerow([currency, rate])

# Візуалізація даних
currencies = list(rates.keys())[:10]  # Візьмемо перші 10 валют
values = [rates[currency] for currency in currencies]

plt.figure(figsize=(10, 5))
plt.bar(currencies, values, color='skyblue')
plt.xlabel('Currency')
plt.ylabel('Rate')
plt.title('Exchange Rates')
plt.show()
