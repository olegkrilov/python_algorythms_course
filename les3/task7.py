"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

from random import randint

random_size = randint(10, 20)
initial_array = [randint(1, 10) for _ in range(0, random_size)]
result = [10, 10]

for val in initial_array:
    if result[0] > val:
        result[0] = val
    elif result[1] > val:
        result[1] = val

print(sorted(initial_array))   # Sorted used here only to better visualize result
print(result)
