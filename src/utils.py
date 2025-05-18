import os
from typing import Any
import json



def get_transaction_from_json(file_path:str) -> list[dict[str, Any]]:
    """
    Функция открытия файла JSON
    """
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            transactions = json.load(json_file)
            if type(transactions) is not list:
                return []
            result = list(filter(bool, transactions))
            return result
    except json.JSONDecodeError:
        return []
