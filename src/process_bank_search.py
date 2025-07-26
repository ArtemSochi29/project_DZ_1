import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Ищет в списке операций те, у которых в описании есть строка search.

    Args:
        data (list[dict]): список словарей с данными о банковских операциях.
        search (str): строка для поиска в описании.

    Returns:
        list[dict]: список словарей, соответствующих условию.
    """
    # Компилируем регулярное выражение для поиска подстроки, игнорируя регистр
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    # Отфильтровываем список, проверяя наличие строки в поле 'описание'
    result = [transaction for transaction in data if
              'описание' in transaction and pattern.search(transaction['описание'])]

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Подсчитывает количество операций для каждой категории из списка categories.

    Args:
        data (list[dict]): список словарей с данными о банковских операциях.
        categories (list): список категорий (строк), по которым нужно подсчитать операции.

    Returns:
        dict: словарь с категориями в качестве ключей и количеством операций в качестве значений.
    """
    # Инициализируем словарь подсчета с нулями для каждой категории
    category_counts = {category: 0 for category in categories}

    for transaction in data:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
                break  # Предполагается, что одна операция относится к одной категории

    return category_counts


import json
import csv
import openpyxl


# Предположим, что у нас есть такие функции (заглушки или реализация):
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_csv(filename):
    transactions = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append(row)
    return transactions


def load_xlsx(filename):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    headers = [cell.value for cell in sheet[1]]
    transactions = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        transaction = dict(zip(headers, row))
        transactions.append(transaction)
    return transactions


def filter_by_status(transactions, status):
    status_upper = status.upper()
    return [tx for tx in transactions if tx.get('status', '').upper() == status_upper]


def sort_transactions(transactions, ascending=True):
    # Предположим, что дата в формате 'dd.mm.yyyy' в поле 'date'
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=not ascending)


def filter_by_description_word(transactions, word):
    word_lower = word.lower()
    return [tx for tx in transactions if 'description' in tx and word_lower in tx['description'].lower()]


def filter_by_currency(transactions, ruble_only):
    # Допустим, что сумма указана в поле 'amount' и есть поле 'currency'
    if ruble_only:
        return [tx for tx in transactions if 'руб' in str(tx.get('amount', '')).lower()]
    return transactions


def print_transactions(transactions):
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего операций: {len(transactions)}")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    for tx in transactions:
        date = tx.get('date', '')
        description = tx.get('description', '')
        amount = tx.get('amount', '')
        print(f"\n{date} {description}\nСумма: {amount}")


# Основная функция программы
def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    filename = ''
    if choice == '1':
        print("Программа: Для обработки выбран JSON-файл.")
        filename = input("Введите путь к JSON-файлу: ")
        transactions = load_json(filename)
    elif choice == '2':
        print("Программа: Для обработки выбран CSV-файл.")
        filename = input("Введите путь к CSV-файлу: ")
        transactions = load_csv(filename)
    elif choice == '3':
        print("Программа: Для обработки выбран XLSX-файл.")
        filename = input("Введите путь к XLSX-файлу: ")
        transactions = load_xlsx(filename)
    else:
        print("Некорректный выбор. Завершение программы.")
        return

    # Запрос статуса
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip()
        if status_input.upper() in valid_statuses:
            print(f"Программа: Операции отфильтрованы по статусу \"{status_input.upper()}\"")
            break
        else:
            print(f"Статус операции \"{status_input}\" недоступен.")

    # Фильтрация по статусу
    filtered_transactions = filter_by_status(transactions, status_input)

    # Вопросы для уточнения
    sort_answer = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_answer == 'да' or sort_answer == 'д':
        order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        ascending = True if 'возрастанию' in order or 'по возрастанию' in order else False
        filtered_transactions = sort_transactions(filtered_transactions, ascending=ascending)

    currency_filter = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if currency_filter == 'да' or currency_filter == 'д':
        filtered_transactions = filter_by_currency(filtered_transactions, ruble_only=True)

    description_filter = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if description_filter == 'да' or description_filter == 'д':
        word = input("Введите слово для фильтрации:\n").strip()
        filtered_transactions = filter_by_description_word(filtered_transactions, word)

    # Вывод итогового списка
    print_transactions(filtered_transactions)


# Запуск программы, если вызывается этот файл
if __name__ == "__main__":
    main()

