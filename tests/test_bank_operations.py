import unittest
from src.process_bank_search import process_bank_operations


class TestProcessBankOperations(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"date": "2025-07-01", "amount": 1000, "description": "Оплата коммунальных услуг"},
            {"date": "2025-07-02", "amount": 200, "description": "Покупка в магазине"},
            {"date": "2025-07-03", "amount": 500, "description": "Оплата телефона"},
            {"date": "2025-07-04", "amount": 1500, "description": "Оплата коммунальных услуг"},
            {"date": "2025-07-05", "amount": 300, "description": "Билет на поезд"},
        ]
        self.categories = ["Оплата", "Покупка", "Билет"]

    def test_counts_correctness(self):
        result = process_bank_operations(self.data, self.categories)
        expected = {"Оплата": 3, "Покупка": 1, "Билет": 1}  # 3 операции с описанием, содержащим 'Оплата'
        self.assertEqual(result, expected)

    def test_category_not_found(self):
        categories = ["Аренда"]
        result = process_bank_operations(self.data, categories)
        self.assertEqual(result, {"Аренда": 0})

    def test_case_insensitivity(self):
        categories = ["оплата", "ПОКУПКА", "билет"]
        result = process_bank_operations(self.data, categories)
        expected = {"оплата": 3, "ПОКУПКА": 1, "билет": 1}
        self.assertEqual(result, expected)

    def test_empty_data(self):
        result = process_bank_operations([], self.categories)
        expected = {"Оплата": 0, "Покупка": 0, "Билет": 0}
        self.assertEqual(result, expected)

    def test_description_missing(self):
        data = [{"date": "2025-07-01", "amount": 1000}]  # без 'description'
        result = process_bank_operations(data, self.categories)
        expected = {"Оплата": 0, "Покупка": 0, "Билет": 0}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
