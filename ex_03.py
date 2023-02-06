"""Параметри функції"""

def hello(name: str) -> str:
    return f'Hello {name}'


name = 'Bill'

result = hello(name)

for n in name:
    print(hello(n))