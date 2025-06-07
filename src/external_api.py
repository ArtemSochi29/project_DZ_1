from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")


def transactions_in_rub(transactions: dict) -> float:
    """ Функция принимает транзакцию и переводит ее в рубли """

    headers = {"apikey": API_KEY}
    amount = transactions["operationAmount"]["amount"]
    code = transactions["operationAmount"]["currency"]["code"]
    if code == "RUB":
        return amount

    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Ошибка: {response.status_code} - {response.text}")

    return round(response.json().get('result'), 2)


if __name__ == "__main__":
    print(transactions_in_rub(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount":
                {
                    "amount": "8221.37",
                    "currency":
                        {
                            "name": "USD",
                            "code": "USD"
                        }
                },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
        ))
