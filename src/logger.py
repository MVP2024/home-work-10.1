import logging
import os


def setup_logger(module_name: str) -> logging.Logger:
    # Создаем папку logs, если она не существует
    os.makedirs('logs', exist_ok=True)

    # Создаем логгер
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)  # Уровень логирования не ниже DEBUG

    # Создаем обработчик для записи в файл
    file_path = os.path.join('logs', f'{module_name}.log')
    # Указание кодировки и перезапись файла при каждом запуске
    file_handler = logging.FileHandler(file_path, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Удаляем все предыдущие обработчики, чтобы избежать дублирования
    if logger.hasHandlers():
        logger.handlers.clear()
    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)
    return logger
