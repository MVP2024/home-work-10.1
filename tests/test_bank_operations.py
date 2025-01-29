from collections import Counter
import pytest

from src.bank_operations import count_transactions_by_category


# Тестирование функции тестирования функции filter_bank_operations.
# Параметризация тестов
@pytest.mark.parametrize("input_data,expected", [
    ([
        {'id': 1, 'description': 'Food'},
        {'id': 2, 'description': 'Transport'},
        {'id': 3, 'description': None},
    ], {'Food': 1, 'Transport': 1, 'Utilities': 0, 'Entertainment': 0}),  # Обновили 'expected'

    ([
        {'id': 1, 'description': 'Utilities'},
        {'id': 2},  # Без описания
    ], {'Food': 0, 'Transport': 0, 'Utilities': 1, 'Entertainment': 0}),  # Обновили 'expected'
])

def test_count_transactions_parametrized(input_data, categories, expected):
    result = count_transactions_by_category(input_data, categories)
    assert result == expected


def test_count_transactions_with_valid_data(transaction_data, categories):
    result = count_transactions_by_category(transaction_data, categories)
    assert result == {'Food': 1, 'Transport': 1, 'Utilities': 1, 'Entertainment': 0}


def test_count_transactions_with_empty_descriptions(transaction_data, categories):
    # Удаляем элементы с пустыми описаниями
    filtered_data = transaction_data[:-2]
    result = count_transactions_by_category(filtered_data, categories)
    assert result == {'Food': 1, 'Transport': 1, 'Utilities': 0, 'Entertainment': 0}


def test_count_transactions_with_nonexistent_category(transaction_data):
    result = count_transactions_by_category(transaction_data, ['Food', 'Transportation'])
    assert result == {'Food': 1, 'Transportation': 0}


def test_count_transactions_with_invalid_input(transaction_data):
    with pytest.raises(ValueError, match="transactions должен быть списком словарей"):
        count_transactions_by_category("not_a_list", ['Food'])

    with pytest.raises(ValueError, match="categories должен быть списком строк"):
        count_transactions_by_category(transaction_data, "not_a_list")


def test_count_transactions_with_mixed_valid_and_invalid(transaction_data, categories):
    mixed_data = [
        {'description': 'Food', 'amount': 100},
        {'description': None, 'amount': 50},  # Отсутствует описание
        'not_a_dict',  # Не словарь
        {'description': 'Utilities', 'amount': 300},
    ]
    result = count_transactions_by_category(mixed_data, categories)
    assert result == {'Food': 1, 'Transport': 0, 'Utilities': 1, 'Entertainment': 0}