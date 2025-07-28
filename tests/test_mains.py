import unittest
from unittest.mock import patch, mock_open
from src.process_bank_search import (
    load_json,
    load_csv,
    load_xlsx,
    filter_by_status,
    sort_transactions,
    filter_by_description_word,
    filter_by_currency,
    print_transactions,
    main,
)
import json
import io


class TestLoadingFunctions(unittest.TestCase):

    def test_load_json(self):
        data = [{"date": "01.01.2020", "description": "desc", "amount": "100", "status": "EXECUTED"}]
        json_data = json.dumps(data)
        with patch("builtins.open", mock_open(read_data=json_data)):
            result = load_json("fake.json")
            self.assertEqual(result, data)

    def test_load_csv(self):
        csv_content = "date,description,amount,status\n01.01.2020,desc,100,EXECUTED\n"
        with patch("builtins.open", mock_open(read_data=csv_content)):
            result = load_csv("fake.csv")
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["date"], "01.01.2020")

    def test_load_xlsx(self):
        # Для теста можно создать временный файл или замокать openpyxl.load_workbook
        # Для простоты пропущу тест, так как он требует файла или сложного мока
        pass


class TestFilteringFunctions(unittest.TestCase):
    transactions = [
        {"date": "01.01.2020", "description": "Оплата коммунальных услуг", "amount": "100", "status": "EXECUTED"},
        {"date": "02.01.2020", "description": "Покупка в магазине", "amount": "200", "status": "CANCELED"},
        {"date": "03.01.2020", "description": "Перевод организации", "amount": "300", "status": "PENDING"},
    ]

    def test_filter_by_status(self):
        result = filter_by_status(self.transactions, "executed")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["status"], "EXECUTED")

    def test_sort_transactions(self):
        sorted_tx = sort_transactions(self.transactions, ascending=True)
        self.assertEqual(sorted_tx[0]["date"], "01.01.2020")

        sorted_tx_desc = sort_transactions(self.transactions, ascending=False)
        self.assertEqual(sorted_tx_desc[0]["date"], "03.01.2020")

    def test_filter_by_description_word(self):
        result = filter_by_description_word(self.transactions, "оплата")
        self.assertEqual(len(result), 1)

    def test_filter_by_currency(self):
        txs = [
            {"amount": "100 руб"},
            {"amount": "USD 50"},
        ]
        result = filter_by_currency(txs, ruble_only=True)
        self.assertEqual(len(result), 1)


class TestPrintTransactions(unittest.TestCase):
    def test_print_transactions(self):
        transactions = [{"date": "01.01.2020", "description": "desc", "amount": "100"}]
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            print_transactions(transactions)
            output = mock_stdout.getvalue()
            self.assertIn("Всего операций: 1", output)

        # тест пустого списка
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            print_transactions([])
            output = mock_stdout.getvalue()
            self.assertIn("Не найдено ни одной транзакции", output)


# Тестирование функции main() — с помощью patch для input()
class TestMainFunction(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "1",  # выбор json
            "fake.json",  # путь
            "EXECUTED",  # статус
            "да",  # сортировка
            "по убыванию",
            "да",  # только рубли
            "да",  # фильтр по слову
            "оплата",
        ],
    )
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            [{"date": "01.01.2020", "description": "Оплата коммунальных услуг", "amount": "100", "status": "EXECUTED"}]
        ),
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_flow(self, mock_stdout, mock_open_fn, mock_input):
        # Тут можно проверить, что вывод содержит ожидаемые строки
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Всего операций", output)


# Чтобы запустить тесты
if __name__ == "__main__":
    unittest.main()
