from typing import Dict
from unittest.mock import MagicMock, patch

import pytest

from src.external_api import transactions_in_rub


@patch("requests.get")
def test_convert_to_rub_usd(mock_get: MagicMock) -> None:
    """Тест успешной конвертации из USD в RUB."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 7500.0}

    transaction: Dict[str, Dict] = {"operationAmount": {"amount": 100.0, "currency": {"code": "USD"}}}
    result = transactions_in_rub(transaction)
    assert result == 7500.0


@patch("requests.get")
def test_convert_to_rub_eur(mock_get: MagicMock) -> None:
    """Тест успешной конвертации из EUR в RUB."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 8500.0}

    transaction: Dict[str, Dict] = {"operationAmount": {"amount": 100.0, "currency": {"code": "EUR"}}}
    result = transactions_in_rub(transaction)
    assert result == 8500.0


def test_convert_to_rub_rub() -> None:
    """Тест: конвертация из RUB в RUB возвращает ту же сумму."""
    transaction: Dict[str, Dict] = {"operationAmount": {"amount": 100.0, "currency": {"code": "RUB"}}}
    result = transactions_in_rub(transaction)
    assert result == 100.0


@patch("requests.get")
def test_error_status(mock_get: MagicMock) -> None:
    mock_get.return_value.status_code = 400
    mock_get.return_value.text = "Bad Request"
    transaction: dict[str, dict] = {"operationAmount": {"amount": 100.0, "currency": {"code": "USD"}}}
    with pytest.raises(Exception) as e:
        transactions_in_rub(transaction)
    assert str(e.value) == "Ошибка: 400 - Bad Request"
