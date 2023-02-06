from typing import List

def split_str(text: str) -> List[str]:
    
    result = []
    if text:
        for i in text:
            result.append(i)
    return result
text1 = 'Hello world'
text2 = ''

print(split_str(text1))
print(split_str(text2))

