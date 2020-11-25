"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

random_size = randint(10, 20)
initial_array = [randint(1, 10) for _ in range(0, random_size)]
result = 0

min_val = (initial_array[0], 1)
max_val = (initial_array[0], 1)

for val in initial_array:
    result += val

    if min_val[0] > val:
        min_val = (val, 1)
    elif min_val[0] == val:
        min_val = (min_val[0], min_val[1] + 1)

    if max_val[0] < val:
        max_val = (val, 1)
    elif max_val[0] == val:
        max_val = (max_val[0], max_val[1] + 1)

result -= (min_val[0] * min_val[1])
result -= (max_val[0] * max_val[1])

print(initial_array)
print(min_val)
print(max_val)
print(result)
