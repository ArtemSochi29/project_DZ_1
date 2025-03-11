import pytest
from src.decorators import log

def sum_two_numbers(a, b):
    return a + b


def test_log():
    @log()
    def sum_two_numbers(a, b):
        return a + b

    result = sum_two_numbers(5, 9)
    assert result == 14

@log()
def sum_two_numbers(a, b):
    return a + b

def test_log_with_different_type_of_arguments(capsys):
    sum_two_numbers("5", 9)
    captured = capsys.readouterr()
    assert "sum_two_numbers" in captured.out

def test_log_captured(capsys) -> None:
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "До выполнения функции\n"



# def test_log_error(capsys) -> None:
#     @log(filename=None)
#     def my_function(x: int, y: int) -> float:
#         """Вывод ошибки"""
#         return x / y
#
#     my_function(1, 0)
#     captured = capsys.readouterr()
#     assert captured.out == "my_function error: ZeroDivisionError. Input: (1, 0), {}\n"
