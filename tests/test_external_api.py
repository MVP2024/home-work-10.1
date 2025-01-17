import os
from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_to_rub


# Устанавливает тестовый API-ключ в переменные окружения, чтобы функция могла его использовать.
@pytest.fixture
def set_api_key():
    os.environ["API_KEY"] = "test_api_key"  # Установите тестовый ключ API


# Проверяет, что функция корректно конвертирует сумму в рубли, когда API возвращает корректный ответ с курсом.
def test_convert_to_rub_success(set_api_key):
    """Тест успешной конвертации валюты в рубли."""
    transaction = {"operationAmount": {"amount": "1000", "currency": {"name": "USD", "code": "USD"}}}

    # Создаем мок-объект для ответа API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}  # Эмулируем успешный ответ с курсом валюты.

    with patch("requests.get", return_value=mock_response):
        result = convert_to_rub(transaction)
        assert result == 75000.0  # 1000 * 75.0


# Проверяет, что функция корректно конвертирует сумму в рубли, когда API возвращает корректный ответ с курсом.
def test_convert_to_rub_already_in_rub(set_api_key):
    """Тест, когда валюта уже в рублях."""
    transaction = {"operationAmount": {"amount": "1000", "currency": {"name": "RUB", "code": "RUB"}}}

    result = convert_to_rub(transaction)
    assert result == 1000.0  # Сумма должна остаться без изменений


# Проверяет, что функция выбрасывает ошибку, когда API не возвращает курс для рубля.
def test_convert_to_rub_invalid_currency(set_api_key):
    """Тест, когда API не возвращает курс для рубля."""
    transaction = {"operationAmount": {"amount": "1000", "currency": {"name": "USD", "code": "USD"}}}

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {}}  # Эмулируем ответ без курса

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Не удалось получить курс для RUB."):
            convert_to_rub(transaction)


# Проверяет, что функция выбрасывает ошибку в случае проблем с API (например, статус 500).
def test_convert_to_rub_api_failure(set_api_key):
    """Тест, когда API возвращает ошибку."""
    transaction = {"operationAmount": {"amount": "1000", "currency": {"name": "USD", "code": "USD"}}}

    mock_response = Mock()
    mock_response.status_code = 500  # Эмулируем ошибку сервера

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Не удалось получить обменный курс."):
            convert_to_rub(transaction)


# Проверяет, что функция выбрасывает ошибку, если в транзакции отсутствует поле operationAmount.
def test_convert_to_rub_missing_operation_amount(set_api_key):
    """Тест, когда в транзакции отсутствует поле operationAmount."""
    transaction = {}

    with pytest.raises(ValueError, match="Транзакция не содержит поле operationAmount."):
        convert_to_rub(transaction)
