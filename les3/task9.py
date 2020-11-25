"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

random_size = randint(5, 10)
limits = [-99, 99]
matrix = []

min_col_values = [limits[1]] * random_size
max_from_min = limits[0]

for i in range(random_size):
    row = [0] * random_size
    the_last_row = i == (random_size - 1)

    for j in range(random_size):
        row[j] = randint(*limits)
        min_col_values[j] = row[j] if row[j] < min_col_values[j] else min_col_values[j]
        if the_last_row:
            max_from_min = min_col_values[j] if min_col_values[j] > max_from_min else max_from_min

    matrix.append(row)

print('*' * (random_size * 4))
for row in matrix:
    print(''.join([f'{val:>4}' for val in row]))

print('-' * (random_size * 4))
print(''.join([f'{val:>4}' for val in min_col_values]))
print(f'MAX VALUE: {max_from_min}')
print('*' * (random_size * 4))
