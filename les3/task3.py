"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

random_size = randint(10, 20)
first_array = [randint(0, 20) for _ in range(0, random_size)]
min_val = None
max_val = None

print([f'{val:>4}' for val in first_array])

for i in range(0, random_size):
    val = first_array[i]
    min_val = (i, val) if (min_val is None) or (min_val[1] < val) else min_val
    max_val = (i, val) if (max_val is None) or (max_val[1] > val) else max_val

first_array[min_val[0]] = max_val[1]
first_array[max_val[0]] = min_val[1]

print([f'{val:>4}' for val in first_array])

