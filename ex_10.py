from ex_08 import factorial
import sys


# print(factorial(5))

def select_mode(param: str) -> int:
    if param == 'A':
        return 10
    if param == 'B':
        return 20

if __name__ == "__main__":
    try:
        print(select_mode(sys.argv[1]))
    except IndexError:
        print('No params')