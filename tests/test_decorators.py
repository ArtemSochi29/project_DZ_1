import pytest
from src.decorators import log


def test_log_captured(capsys) -> None:
    @log(filename=None)
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"

def test_log_error(capsys) -> None:
    @log(filename=None)
    def my_function(x: int, y: int) -> float:
        """Вывод ошибки"""
        return x / y

    my_function(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: ZeroDivisionError. Input: (1, 0), {}\n"
