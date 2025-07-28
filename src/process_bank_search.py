from src.generators import filter_by_currency, filter_by_currency_in_csv
from src.processing import filter_by_state, sort_by_date
from src.transactions import process_bank_search
from src.transactions_csv_excel import transactions_csv_read, transactions_excel_read
from src.utils import load_transactions
from src.widget import mask_account_card, get_date


def print_transactions(transactions, is_json):
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего операций: {len(transactions)}")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    for tx in transactions:
        date = tx.get("date", "")
        description = tx.get("description", "")
        if is_json:
            amount = tx.get("operationAmount", {}).get("amount", "")
            currency_name = tx.get("operationAmount", {}).get("currency", {}).get("name", "")
        else:
            amount = tx.get("amount", "")
            currency_name = tx.get("currency_name", "")
        if "from" in tx:
            # 12.11.2019 Перевод с карты на карту
            # MasterCard 7771 27 ** ** ** 3727 -> Visa Platinum 1293 38 ** ** ** 9203
            # Сумма: 130 USD
            print(
                f"\n{get_date(date)} {description}\n"
                f"{mask_account_card(tx.get('from', ''))} -> {mask_account_card(tx.get('to', ''))}\n"
                f"Сумма: {amount} {currency_name}"
            )
        else:
            # 08.12.2019 Открытие вклада
            # Счет ** 4321
            # Сумма: 40542 руб.
            print(
                f"\n{get_date(date)} {description}\n"
                f"{mask_account_card(tx.get('to', ''))}\n"
                f"Сумма: {amount} {currency_name}"
            )
    return


# Основная функция программы
def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    is_json = False

    while True:
        choice = input("Пользователь: ").strip()
        if choice == "1":
            print("Программа: Для обработки выбран JSON-файл.")
            file_patch = "/Users/avrorabaranova/PycharmProjects/Homework/data/operations.json"
            transactions = load_transactions(file_patch)
            is_json = True
            break
        elif choice == "2":
            print("Программа: Для обработки выбран CSV-файл.")
            file_patch = "/Users/avrorabaranova/PycharmProjects/Homework/data/transactions.csv"
            transactions = transactions_csv_read(file_patch)
            break
        elif choice == "3":
            print("Программа: Для обработки выбран XLSX-файл.")
            file_patch = "/Users/avrorabaranova/PycharmProjects/Homework/data/transactions.xlsx"
            transactions = transactions_excel_read(file_patch)
            break
        else:
            print("Некорректный выбор.")

    # Запрос статуса
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).strip()
        if state.upper() in valid_statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{state.upper()}"')
            filtered_transactions = filter_by_state(transactions, state)
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    # Вопросы для уточнения
    while True:
        sort_answer = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if sort_answer == "да" or sort_answer == "д":
            while True:
                order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
                if order in ("возрастанию", "по возрастанию"):
                    filtered_transactions = sort_by_date(filtered_transactions, sort_order=False)
                    break
                elif order in ("убыванию", "по убыванию"):
                    filtered_transactions = sort_by_date(filtered_transactions)
                    break
                else:
                    print("Введены не корректные данные")
            break
        elif sort_answer == "нет" or sort_answer == "н":
            break
        else:
            print("Введены не корректные данные")

    while True:
        currency_filter = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
        if currency_filter in ("да", "д"):
            if is_json:
                filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
                break
            else:
                filtered_transactions = list(filter_by_currency_in_csv(filtered_transactions, "RUB"))
                break
        elif currency_filter in ("нет", "н"):
            break
        else:
            print("Введены не корректные данные")

    while True:
        description_filter = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
        )
        if description_filter in ("да", "д"):
            word = input("Введите слово для фильтрации:\n").strip()
            filtered_transactions = process_bank_search(filtered_transactions, word)
            break
        elif description_filter in ("нет", "н"):
            break
        else:
            print("Введены не корректные данные")

    # Вывод итогового списка
    print_transactions(filtered_transactions, is_json)


# Запуск программы, если вызывается этот файл
if __name__ == "__main__":
    main()
