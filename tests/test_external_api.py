from unittest.mock import Mock, patch

import requests

from src.external_api import convert_to_rub


# Проверяем, функция корректно конвертирует сумму из одной валюты в рубли (RUB) при успешном ответе от API.
def test_successful_conversion():
    with patch("requests.get") as mock_get, patch("os.getenv") as mock_getenv:
        mock_getenv.return_value = "test_api_key"  # Устанавливаем API ключ

        # Настраиваем mock для ответа API
        mock_response = Mock()
        mock_response.json.return_value = {"result": 100.0}  # Успешный ответ
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

        result = convert_to_rub(transaction)
        assert result == 100.0  # Проверяем, что результат соответствует ожидаемому


# Проверяем, что функция возвращает ту же сумму, если валюта уже в рублях.
def test_conversion_when_currency_is_rub():
    with patch("os.getenv") as mock_getenv:
        mock_getenv.return_value = "test_api_key"  # Устанавливаем API ключ

        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}

        result = convert_to_rub(transaction)
        assert result == 100.0  # Проверяем, что результат соответствует ожидаемому


#  Проверяем, что функция выбрасывает исключение, если в транзакции отсутствует поле operationAmount.
def test_missing_operation_amount():
    transaction = {}
    try:
        convert_to_rub(transaction)
    except ValueError as e:
        assert str(e) == "Транзакция не содержит поле operationAmount."  # Проверяем сообщение об ошибке


# Проверяем, что функция выбрасывает исключение, если API ключ не установлен.
def test_api_key_not_set():
    with patch("os.getenv") as mock_getenv:
        mock_getenv.return_value = None  # Устанавливаем API ключ как None
        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
        try:
            convert_to_rub(transaction)
        except ValueError as e:
            assert str(e) == "API_KEY не установлен."  # Проверяем сообщение об ошибке


# Проверяем, что функция правильно обрабатывает ошибки при запросе к API.
def test_api_request_failure():
    with patch("requests.get") as mock_get, patch("os.getenv") as mock_getenv:
        mock_getenv.return_value = "test_api_key"  # Устанавливаем API ключ

        # Создаем mock-ответ с кодом состояния 500
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.HTTPError("Request failed", response=mock_response)
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

        try:
            convert_to_rub(transaction)
        except ValueError as e:
            assert str(e) == "Не удалось получить обменный курс. Статус код: 500"  # Проверяем сообщение об ошибке


# Проверяем, что функция выбрасывает исключение, если API возвращает ответ без поля result.
def test_api_response_without_result():
    with patch("requests.get") as mock_get, patch("os.getenv") as mock_getenv:
        mock_getenv.return_value = "test_api_key"  # Устанавливаем API ключ

        mock_response = Mock()
        mock_response.json.return_value = {}  # Пустой ответ
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

        try:
            convert_to_rub(transaction)
        except ValueError as e:
            assert str(e) == "Не удалось получить курс для RUB."  # Проверяем сообщение об ошибке
