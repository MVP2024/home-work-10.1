import time

import pytest

from .conftest import add, divide, log, raise_error


@pytest.mark.parametrize(
    "a, b, expected, should_raise",
    [
        (3, 4, 0.75, False),  # правильное ожидание для 3 / 4
        (10, 2, 5, False),  # 10 / 2 = 5
        (10, 0, None, True),  # деление на ноль
    ],
)
def test_divide_and_add(capsys, a, b, expected, should_raise):
    if should_raise:
        with pytest.raises(ZeroDivisionError):
            divide(a, b)

        # Перехватываем вывод
        captured = capsys.readouterr()
        output = captured.out

        assert "Начало divide" in output
        assert "divide) error: ZeroDivisionError" in output
        assert f"Inputs: ({a}, {b})" in output
    else:
        result = divide(a, b)
        assert result == expected

        # Перехватываем вывод
        captured = capsys.readouterr()
        output = captured.out

        assert "Начало divide" in output
        assert "divide ok." in output
        assert f"Возвращаемое значение {expected}" in output


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (5, 7, 12),
    ],
)
def test_add(capsys, a, b, expected):
    result = add(a, b)
    assert result == expected

    # Перехватываем вывод
    captured = capsys.readouterr()
    output = captured.out

    assert "Начало add" in output
    assert "add ok." in output
    assert f"Возвращаемое значение {expected}" in output


@pytest.mark.parametrize("should_raise", [True, False])
def test_raise_error(capsys, should_raise):
    if should_raise:
        with pytest.raises(ValueError):
            raise_error()

        # Перехватываем вывод
        captured = capsys.readouterr()
        output = captured.out

        assert "Начало raise_error" in output
        assert "raise_error) error: ValueError" in output
        assert "Inputs: ()" in output
        assert "Ошибка: This is an error" in output


def test_log_with_delay(capsys):
    @log(time_delay=1)
    def slow_add(a, b):
        return a + b

    start_time = time.time()
    result = slow_add(2, 3)
    end_time = time.time()

    assert result == 5
    assert end_time - start_time >= 1  # Проверяем, что задержка была как минимум 1 секунда

    # Перехватываем вывод
    captured = capsys.readouterr()
    output = captured.out

    assert "Начало slow_add" in output
    assert "slow_add ok." in output
    assert "Возвращаемое значение 5" in output
