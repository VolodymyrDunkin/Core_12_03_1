"""Змінна кількість параметрів"""

# a, b, *c, d = [1, 2, 45, 78, 89]

# print(a, b, c, d)

# a, b, *c = [1, 2, 3, 4, 5]

# print(a, b, c)

def calc_sum(num1: int=5, *nums, **knums) -> int:
    print(nums)
    result = 0
    for num in nums:
        result += num
    result += num1
    
    print(knums)
    for _, item in knums.items():
        result += item
    
    return result

nums = [1, 1, 1, 1, 1]

k_nums = {'first': 1, 'second': 2, 'third': 3}

print(calc_sum(5, *nums, **k_nums))