import os
import  logging
from typing import List, Dict, Any
import json
from venv import logger

import requests
from src.external_api import API_KEY
from src.settings import BASE_DIR, LOGS_DIR


name_file = "utils.log"
log_file = LOGS_DIR / name_file

utils_logger = logging.getLogger(name_file)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s: %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)



def load_transactions(file_path: str, utils_logger=None) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON файла.

    Args:
        file_path: Путь к JSON файлу

    Returns:
        Список словарей с транзакциями или пустой список при ошибках
    """
    if not os.path.exists(file_path):
        return []

    if not os.path.exists(file_path):
        utils_logger.info("Файл не найдет, выводит пусто список")
        return []


    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Явно проверяем, что данные - это список
            return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        # Логирование ошибки может быть полезно для отладки
        print(f"Error loading transactions from {file_path}: {str(e)}")
        return []
