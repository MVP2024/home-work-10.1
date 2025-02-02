import pytest

from src.bank_operations import count_operations_by_category, filter_bank_operations


# Тестирование функции filter_bank_operations
def test_filter_bank_operations():
    transactions_3 = [
        {"id": "1", "description": "Перевод с карты на карту"},
        {"id": "2", "description": "Открытие вклада"},
        {"id": "3", "description": "Закрытие вклада"},
        {"id": "4", "description": "Перевод на счет"},
        {"id": "5", "description": "Оплата услуг"},
    ]

    # Тест 1: Проверка точного совпадения
    result = filter_bank_operations(transactions_3, "Перевод с карты на карту")
    assert len(result) == 1 and result[0]["id"] == "1", "Тест 1 не пройден"

    # Тест 2: Проверка частичного совпадения
    result = filter_bank_operations(transactions_3, "перевод")
    assert len(result) == 2, "Тест 2 не пройден"

    # Тест 3: Проверка с пустой строкой
    result = filter_bank_operations(transactions_3, "")
    assert result == [], "Тест 3 не пройден"

    # Тест 4: Проверка с несуществующим ключевым словом
    result = filter_bank_operations(transactions_3, "неизвестное слово")
    assert result == [], "Тест 4 не пройден"

    # Тест 5: Проверка с неправильным типом transactions
    try:
        filter_bank_operations("неправильный тип", "перевод")
    except ValueError:
        pass  # Ожидаем исключение

    # Тест 6: Проверка с неправильным типом search_str
    try:
        filter_bank_operations(transactions_3, 123)
    except ValueError:
        pass  # Ожидаем исключение

    # Тест 7: Проверка с транзакцией, которая не является словарем
    transactions_with_non_dict = [
        {"id": "1", "description": "Перевод с карты на карту"},
        "не словарь",  # Неверный элемент
        {"id": "2", "description": "Открытие вклада"},
    ]
    result = filter_bank_operations(transactions_with_non_dict, "перевод")
    assert len(result) == 1, "Тест 7 не пройден"


# Тестирование функции count_operations_by_category
def test_count_operations_by_category():
    transactions = [
        {"description": "Покупка в магазине"},
        {"description": "Покупка продуктов"},
        {"description": "Топливо для автомобиля"},
        {"description": "Подписка на Ж"},
        {"description": "Дискотека"},
    ]
    categories = ["еда", "покупка", "топливо", "досуг"]

    expected_result = {"еда": 0, "покупка": 2, "топливо": 1, "досуг": 0}
    assert count_operations_by_category(transactions, categories) == expected_result


def test_empty_transactions():
    transactions = []
    categories = ["еда", "товары"]

    expected_result = {"еда": 0, "товары": 0}
    assert count_operations_by_category(transactions, categories) == expected_result


def test_no_categories():
    transactions = [{"description": "Покупка в магазине"}, {"description": "Покупка продуктов"}]
    categories = []

    expected_result = {}
    assert count_operations_by_category(transactions, categories) == expected_result


def test_non_dict_transaction():
    transactions = [{"description": "Покупка в магазине"}, "Не словарь"]
    categories = ["еда"]

    with pytest.raises(ValueError) as excinfo:
        count_operations_by_category(transactions, categories)
    assert str(excinfo.value) == "Каждый элемент transactions должен быть словарем."


def test_case_insensitivity():
    transactions = [
        {"description": "Покупка в магазине"},
        {"description": "Покупка продуктов"},
        {"description": "Топливо для автомобиля"},
    ]
    categories = ["ЕДА", "покупка", "ТОПЛИВО"]

    expected_result = {"ЕДА": 0, "покупка": 2, "ТОПЛИВО": 1}
    assert count_operations_by_category(transactions, categories) == expected_result
