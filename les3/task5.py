"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значениеи позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

from random import randint

random_size = randint(10, 20)
initial_array = [randint(-100, 100) for _ in range(0, random_size)]
result = 0

for val in initial_array:
    if val < 0:
        if not result or val > result:
            result = val

print(sorted(initial_array))  # Sorted used here only to better visualize result
print(result)
