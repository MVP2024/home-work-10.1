import logging
import os


def setup_logger(module_name: str) -> logging.Logger:
    # Определяем абсолютный путь к корню проекта
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', ))
    logs_dir = os.path.join(project_root, "logs")

    # Создаем папку logs, если она не существует
    os.makedirs(logs_dir, exist_ok=True)

    # Настраиваем формат логирования
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Создаем логгер
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)  # Уровень логирования

    # Создаем обработчик для записи логов в файл с указанием кодировки и режима 'w'
    log_file_path = os.path.join(logs_dir, f"{module_name}.log")
    file_handler = logging.FileHandler(log_file_path, mode='w', encoding='utf-8')  # Указываем кодировку и режим
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger
