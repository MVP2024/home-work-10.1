import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму из указанной валюты в рубли (RUB).

    :param transaction: Словарь, представляющий транзакцию, который должен содержать
                       поле "operationAmount" и "amount" (число в виде строки)
                       и "currency" (словарь с полем "code", указывающим код валюты).

    :raises ValueError: Если транзакция не содержит поле "operationAmount".
                        Если API не возвращает курс для RUB.
                        Если не удается получить обменный курс.

    :return: Конвертированная сумма в рублях (RUB).
    """
    if "operationAmount" not in transaction:
        raise ValueError("Транзакция не содержит поле operationAmount.")

    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    # Если валюта уже RUB, просто возвращаем сумму
    if currency_code == "RUB":
        return amount

    # Формируем URL для запроса к API конвертации
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не установлен.")

    api_url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    headers = {"apikey": api_key}

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Вызывает исключение для плохих статусов
    except requests.RequestException as e:
        # Если запрос не удался, добавляем статус код в сообщение об ошибке
        if response is not None:
            raise ValueError(f"Не удалось получить обменный курс. Статус код: {response.status_code}") from e
        raise ValueError("Не удалось получить обменный курс.") from e

    data = response.json()
    if "result" in data:
        converted_amount = data["result"]
        return converted_amount
    else:
        raise ValueError(f"Не удалось получить курс для {currency_code}.")
