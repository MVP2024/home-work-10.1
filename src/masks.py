from typing import Union

from src.decorators import log
from src.logger import setup_logger

# Настройка логгера для модуля masks
logger = setup_logger('masks')

# Логируем инициализацию модуля
logger.info("Инициализация модуля masks")


@log("mylog.txt")
def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает замаскированный номер"""
    logger.debug(f'Получен номер карты: {card_number}')  # Логируем входные данные

    # Проверяем, является ли строка пустой
    if not card_number:
        logger.error("Ошибка: входная строка пустая.")  # Логируем ошибку
        return "Ошибка: входная строка пустая."

    # Проверяем длину номера карты
    if len(card_number) < 16:
        logger.error("Ошибка: слишком короткий номер карты.")  # Логируем ошибку
        return "Ошибка: слишком короткий номер карты."

    elif len(card_number) > 16:
        logger.error("Ошибка: слишком длинный номер карты.")  # Логируем ошибку
        return "Ошибка: слишком длинный номер карты."

    # Проверяем, если в номере карты присутствуют кроме цифр, другие символы
    if not card_number.isdigit():
        logger.error("Ошибка: присутствуют другие символы в номере карты.")  # Логируем ошибку
        return "Ошибка: присутствуют другие символы в номере карты."

    # Маскируем номер карты
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    logger.info(f'Замаскированный номер карты: {masked_card_number}')  # Логируем успешный результат

    # Возвращаем замаскированный номер в формате XXXX XX** **** XXXX.
    return masked_card_number


@log("mylog.txt")
def get_mask_account(account_number: Union[str]) -> Union[str, ValueError]:
    """Функция принимает на вход номер счёта и возвращает замаскированный счёт"""
    logger.debug(f'Получен номер счёта: {account_number}')  # Логируем входные данные

    # Проверяем, является ли строка пустой
    if not account_number:
        logger.error("Ошибка: входная строка пустая.")  # Логируем ошибку
        return "Ошибка: входная строка пустая."

    # Проверяем длину номера счёта
    if len(account_number) < 16:
        logger.error("Ошибка: слишком короткий номер счёта.")  # Логируем ошибку
        return "Ошибка: слишком короткий номер счёта."

    elif len(account_number) > 16:
        logger.error("Ошибка: слишком длинный номер счёта.")  # Логируем ошибку
        return "Ошибка: слишком длинный номер счёта."

    # Проверяем, если в номере счёта присутствуют кроме цифр, другие символы
    if not account_number.isdigit():
        logger.error("Ошибка: присутствуют другие символы в счёте.")  # Логируем ошибку
        return "Ошибка: присутствуют другие символы в счёте."

    # Маскируем номер счёта
    masked_account = "**" + account_number[-4:]
    logger.info(f'Замаскированный номер счёта: {account_number}')  # Логируем успешный результат

    # Возвращаем замаскированный номер
    return masked_account
