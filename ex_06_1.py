def calc_many(*args: list[int], **kwargs:dict[str, int]) -> int:
    result = 0
    for i in args:
        result = result + i
    
    for i in kwargs.values():
        result += i
    
    return result

nums = [1, 1, 1, 1, 1]

k_nums = {'1': 1, '2': 2, '3': 3, '4': 4}

print(calc_many(*nums, **k_nums))