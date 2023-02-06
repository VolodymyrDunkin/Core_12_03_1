""""Локальні та глобальні зманні"""

name = 'Bill'

def lower_string(text: str) -> str:
    name = text
    return name.lower()

# print(lower_string(name))
# print(name)

def global_lower_str(text: str) -> str:
    global name
    name = text.lower()
    return name

global_lower_str(name)

print(name)