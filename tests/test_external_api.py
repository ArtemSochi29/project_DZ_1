from typing import Dict

import pytest
import requests
from unittest.mock import MagicMock, patch
from src.external_api import external_api



@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get: MagicMock) -> None:
    """Тест успешной конвертации из USD в RUB."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500.0}

    transaction: Dict[str, Dict] = {
        "operationAmount": {
            "amount": 100.0,
            "currency": {
                "code": "USD"
            }
        }
    }
    result = external_api(transaction)
    assert result == {"result": 7500.0}


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get: MagicMock) -> None:
    """Тест успешной конвертации из EUR в RUB."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 8500.0}

    transaction: Dict[str, Dict] = {
        "operationAmount": {
            "amount": 100.0,
            "currency": {
                "code": "EUR"
            }
        }
    }
    result = external_api(transaction)
    assert result == {"result": 8500.0}

def test_convert_to_rub_rub() -> None:
    """Тест: конвертация из RUB в RUB возвращает ту же сумму."""
    transaction: Dict[str, Dict] = {
        "operationAmount": {
            "amount": 100.0,
            "currency": {
                "code": "RUB"
            }
        }
    }
    result = external_api(transaction)
    assert result == 100.0