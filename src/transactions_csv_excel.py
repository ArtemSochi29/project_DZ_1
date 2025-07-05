from typing import Any, Dict, List, cast

import pandas as pd


def transactions_csv_read(file_path: str) -> List[Dict[str, Any]]:
    """
    Функция принимает файл csv и выводит список словарей
    :param file_path:
    :return:
    """
    try:
        df_transactions = pd.read_csv(file_path, delimiter=";")
        list_transactions = df_transactions.to_dict(orient="records")
        return cast(List[Dict[str, Any]], list_transactions)

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл: {file_path} не найден")


def transactions_excel_read(file_path: str) -> List[Dict[str, Any]]:
    """
    Функция принимает файл excel и выводит список словарей
    :param file_path:
    :return:
    """
    try:
        df_transactions = pd.read_excel(file_path)
        list_transactions = df_transactions.to_dict(orient="records")
        return cast(List[Dict[str, Any]], list_transactions)

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл: {file_path} не найден")
