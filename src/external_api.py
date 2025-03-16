import requests
from dotenv import load_dotenv
import os



load_dotenv()
API_KEY = os.getenv("API_KEY")
def external_api(transactions: dict) -> float:
    headers = {"apikey": API_KEY}
    amount = transactions["operationAmount"] ["amount"]
    code = transactions["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    response = requests.get(url, headers=headers)
    return response.json()

print(external_api(
{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
))