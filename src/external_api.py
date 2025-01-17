import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    if "operationAmount" not in transaction:
        raise ValueError("Транзакция не содержит поле operationAmount.")

    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    # Если валюта уже RUB, просто возвращаем сумму
    if currency_code == "RUB":
        return amount

    # Формируем URL для запроса к API
    api_key = os.getenv("API_KEY")
    api_url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency_code}&symbols=RUB"

    print(f"Запрос к API: {api_url}")  # Отладочное сообщение для проверки корректного url.

    headers = {"apikey": api_key}

    response = requests.get(api_url, headers=headers)
    print(f"Статус код ответа: {response.status_code}")  # Отладочное сообщение для проверки кода.
    print(f"Ответ от API: {response.text}")  # Отладочное сообщение от API.

    if response.status_code == 200:
        data = response.json()
        if "rates" in data and "RUB" in data["rates"]:
            rate = data["rates"]["RUB"]
            converted_amount = amount * rate
            print(f"Конвертированная сумма: {converted_amount} RUB")  # Полученная сумма в рублях.
            return converted_amount
        else:
            raise ValueError("Не удалось получить курс для RUB.")  # Ошибка, если нет курса для рубля.
    else:
        raise ValueError("Не удалось получить обменный курс.")
