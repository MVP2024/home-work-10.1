import pytest

from src.processing import filter_by_state, sort_by_date


# Тестирование функции `filter_by_state`
@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 1, "state": "EXECUTED"},
                {"id": 5, "state": "EXECUTED"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 2, "state": "CANCELED"},
            ],
        ),
        (
            "PENDING",
            [
                {"id": 3, "state": "PENDING"},
            ],
        ),
        ("UNKNOWN", "Ошибка: значение 'UNKNOWN' не найдено для ключа 'state'."),
    ],
)
def test_filter_by_state(sample_data, state, expected):
    assert filter_by_state(sample_data, state) == expected


def test_empty_data():
    assert filter_by_state([], "EXECUTED") == "Ошибка: входная строка пустая."


def test_missing_state_key():
    assert filter_by_state([{"id": 1}], "EXECUTED") == "Ошибка: такого ключа нет."


def test_none_state_value():
    assert (
        filter_by_state([{"id": 1, "state": None}],
                        "EXECUTED") == "Ошибка: значение 'EXECUTED' не найдено для ключа 'state'.")


# Тестирование функции `sort_by_date`
@pytest.mark.parametrize(
    "data, reverse, expected",
    [
        (
            [
                {"date": "2023-01-01"},
                {"date": "2022-12-31"},
                {"date": "2023-01-02"},
                {"date": "2022-12-30"},
            ],
            True,
            [
                {"date": "2023-01-02"},
                {"date": "2023-01-01"},
                {"date": "2022-12-31"},
                {"date": "2022-12-30"},
            ],
        ),
        (
            [
                {"date": "2023-01-01"},
                {"date": "2022-12-31"},
            ],
            False,
            [
                {"date": "2022-12-31"},
                {"date": "2023-01-01"},
            ],
        ),
        ([], True, ValueError),  # Пустой список
        ([{"date": None}], True, ValueError),  # Значение None
        ([{"bad_key": "2023-01-01"}], True, ValueError),  # Отсутствие ключа "date"
    ],
)
def test_sort_by_date(data, reverse, expected):
    if isinstance(expected, list):
        assert sort_by_date(data, reverse) == expected
    else:
        with pytest.raises(expected):
            sort_by_date(data, reverse)


# Дополнительные тесты на ошибки
def test_empty_list():
    with pytest.raises(ValueError, match="Ошибка: передан пустой список."):
        sort_by_date([])


def test_missing_date_key():
    with pytest.raises(ValueError, match="Ошибка: отсутствует ключ 'date'"):
        sort_by_date([{"not_date": "2023-01-01"}])


def test_none_date_value():
    with pytest.raises(ValueError, match="Ошибка: значение по ключу 'date'"):
        sort_by_date([{"date": None}])
