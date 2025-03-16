import os
from typing import Any

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()

api_key = os.getenv("API_KEY")


def convert_to_rub(amount: float, currency: str) -> float:
    """Функция принимает значение в долларах или евро, обращается к API и возвращает конвертацию в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert{amount}"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate")

    else:
        json_result = response.json()
        rub_amount = json_result["result"]
        return rub_amount