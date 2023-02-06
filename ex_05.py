"""Ключові аргументи"""


def sum_int(num1: int, num2: int=10, num3: int|None = None) -> int:
    if num3:
        return num1 + num2 + num3 
    result = num1 + num2
    return result


print(sum_int(1, 20, 300))