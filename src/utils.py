import os
import logging
from typing import List, Dict, Any
import json
from src.generators import transactions
from src.settings import LOGS_DIR


name_file = "utils"
log_file = LOGS_DIR / "utils.log"

utils_logger = logging.getLogger(name_file)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s: %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def load_transactions(file_path: str, utils_logger=None) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON файла.
    Args:
        file_path: Путь к JSON файлу
    Returns:
        Список словарей с транзакциями или пустой список при ошибках
    """
    if not os.path.exists(file_path):
        utils_logger.error("Файл не найдет, выводит пусто список")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Явно проверяем, что данные - это список
            if not isinstance(transactions, list):
                utils_logger.error("Файл содержит не список")
                return []
            utils_logger.info("Функция прошла успешно")
            return data
    except json.JSONDecodeError:
        utils_logger.error("Файл не найдет, выводит пусто список")
        return []
    except Exception:
        # Логирование ошибки может быть полезно для отладки
        utils_logger.error("Файл не найдет, выводит пусто список")
        return []
