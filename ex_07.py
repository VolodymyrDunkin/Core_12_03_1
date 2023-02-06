"""Контейнери для зберігання результатів"""
from typing import List

def split_str(text: str) -> List[str]:
    result = []
    if text:
        for i in text:
            result.append(i)
    return result


text1 = 'Hello world'

text2 = ''

# print(split_str(text1))
# print(split_str(text2))


def check_result(num1: int, num2: int) -> tuple[bool, int]:
    if num1 > num2:
        return True, num1
    return False, num2

n1 = 10
n2 = 20
n3 = 5

# result = check_result(n1, n2)

# if result[0]:
#     print('Ok')


GRADE = {
    'F': 1,
    'FX': 2,
    'E': 3,
    'D': 3,
    'C': 4,
    'B': 5,
    'A': 5
}

def get_grade(grade: str) -> dict[str, int]:
    for k in GRADE:
        if k == grade:
            return {k: GRADE[k]}
    return {}


print(get_grade('XX'))