import json
from src.utils import get_transaction_from_json
import pytest
from typing import Any
import os


@pytest.fixture
def transactions() -> list[dict[str, Any]]:
    return [
        {"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}},
        {"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}},
        {"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}},
    ]

def test_get_transaction_from_json(transactions) -> None:
    file_path = "test.json"
    try:
        with open(file_path, "w", encoding="utf-8") as file_json:
            json.dump(transactions, file_json, indent=4, ensure_ascii=False)
        assert get_transaction_from_json(file_path) == transactions
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

def test_get_transaction_from_json_empty_list():
    file_path = "test.json"
    transactions = []
    try:
        with open(file_path, "w", encoding="utf-8") as file_json:
            json.dump(transactions, file_json, indent=4, ensure_ascii=False)
        assert get_transaction_from_json(file_path) == transactions
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

def test_get_transaction_from_json_invalid_json():
    file_path = "test.json"
    transactions = "Error"
    try:
        with open(file_path, "w", encoding="utf-8") as file_json:
            file_json.write(transactions)
        assert get_transaction_from_json(file_path) == []
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

def test_get_transaction_from_json_not_list():
    file_path = "test.json"
    transactions = "Error"
    try:
        with open(file_path, "w", encoding="utf-8") as file_json:
            json.dump(transactions, file_json, indent=4, ensure_ascii=False)
        assert get_transaction_from_json(file_path) == []
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

def test_none_file_path():
    file_path = "test.json"
    assert get_transaction_from_json(file_path) == []
