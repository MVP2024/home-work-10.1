from unittest.mock import mock_open, patch

from src.utils import load_transactions


# Проверяет, что функция корректно загружает данные из файла, когда данные валидны.
# Мы используем mock_open для эмуляции открытия файла и возвращаемого содержимого.
def test_load_transactions_success():
    """Тест успешной загрузки транзакций из файла JSON."""
    mock_data = '[{"id": 1, "operationAmount": {"amount": "1000", "currency": {"name": "USD", "code": "USD"}}}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions("fake_path.json")
        assert len(result) == 1
        assert result[0]["id"] == 1


# Проверяет, что функция возвращает пустой список, если файл содержит пустой массив.
def test_load_transactions_empty():
    """Тест загрузки пустого списка из файла JSON."""
    mock_data = "[]"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions("fake_path.json")
        assert result == []


# Проверяет, что функция возвращает пустой список, если файл не найден, используя side_effect=FileNotFoundError.
def test_load_transactions_file_not_found():
    """Тест обработки ошибки, когда файл не найден."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transactions("fake_path.json")
        assert result == []


# Проверяет, что функция возвращает пустой список, если файл содержит некорректный JSON.
def test_load_transactions_invalid_json():
    """Тест обработки ошибки при некорректном JSON."""
    mock_data = "{not_a_list}"  # Некорректный JSON
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transactions("fake_path.json")
        assert result == []
