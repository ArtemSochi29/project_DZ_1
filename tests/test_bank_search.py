import unittest
from src.process_bank_search import process_bank_search



class TestBankSearch(unittest.TestCase):
    def setUp(self):
        # Пример данных для тестов
        self.data = [
            {'дата': '2025-07-01', 'сумма': 1000, 'описание': 'Оплата коммунальных услуг'},
            {'дата': '2025-07-02', 'сумма': 200, 'описание': 'Покупка в магазине'},
            {'дата': '2025-07-03', 'сумма': 500, 'описание': 'Оплата телефона'},
            {'дата': '2025-07-04', 'сумма': 1500, 'описание': 'Оплата коммунальных услуг'},
            {'дата': '2025-07-05', 'сумма': 300, 'описание': 'Билет на поезд'},
        ]

    def test_search_found(self):
        # Тест, когда совпадения есть
        result = process_bank_search(self.data, 'коммунальных')
        self.assertEqual(len(result), 2)
        self.assertTrue(all('коммунальных' in item['описание'].lower() for item in result))

    def test_search_not_found(self):
        # Тест, когда совпадений нет
        result = process_bank_search(self.data, 'авто')
        self.assertEqual(result, [])

    def test_search_case_insensitive(self):
        # Проверка нечувствительности к регистру
        result_upper = process_bank_search(self.data, 'КОММУНАЛЬНЫХ')
        result_lower = process_bank_search(self.data, 'коммунальных')
        self.assertEqual(result_upper, result_lower)

    def test_empty_data(self):
        # Проверка, что при пустом списке возвращается пустой список
        self.assertEqual(process_bank_search([], 'любое'), [])

    def test_no_description_key(self):
        # Проверка, что объекты без ключа 'описание' игнорируются
        data = [{'дата': '2025-07-01', 'сумма': 1000}]
        result = process_bank_search(data, 'любое')
        self.assertEqual(result, [])

    def test_partial_match(self):
        # Проверка, что частичное совпадение ищется
        result = process_bank_search(self.data, 'плат')
        self.assertEqual(len(result), 3)  # 'Оплата' в трех записях


if __name__ == '__main__':
    unittest.main()
