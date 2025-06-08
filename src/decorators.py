from pathlib import Path
from typing import Any, Callable, Optional

current_dir = Path(__file__).parent.parent.resolve()
log_scripts = current_dir / "data" / "mylog.txt"


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который логирует начало и конец выполнения функции, а также ее результаты и возникшие ошибки"""

    def logging(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print("До выполнения функции")
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(log_scripts, "a") as file:
                        file.write(f'Function {func.__name__}: {"a"}. Inputs: {args}, kwargs: {kwargs}.')
                else:
                    with open(log_scripts, "a") as file:
                        file.write(f"{func.__name__} ok\n")
            except Exception as e:
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        print(f"Function {func.__name__}: {e}. Inputs: {args}, kwargs: {kwargs}.")
                else:
                    print(f"Функция: {func.__name__} - ERROR: {e} with inputs: {args}, {kwargs}")
                result = None
                print("После выполнения функции")
            return result

        return wrapper

    return logging
