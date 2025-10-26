# main.py
from logger_decorator import logger


@logger("INFO")
def say_hello(name):
    print(f"Привіт, {name}!")


@logger("WARNING")
def divide(a, b):
    print("Ділю числа...")
    return a / b


@logger("ERROR")
def test_error():
    raise ValueError("Це тестова помилка")


if __name__ == "__main__":
    say_hello("Паша")
    print()

    divide(10, 2)
    print()

    try:
        test_error()
    except:
        pass
