"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

matrix = []
cols_len = 4
rows_len = 4
i = 0

# Notice: please, for better visual representation use integers in range [0, 99]
while i < rows_len:
    _sum = 0
    _i = 0
    _row = [0] * 4

    while _i < cols_len:
        _row[_i] += int(input(f'Input value for (x: {_i}; y: {i}) >>> '))
        _sum += _row[_i]
        _i += 1

    else:
        _row.append(_sum)

    matrix.append(_row)
    i += 1

else:
    print('*' * 24)
    for row in matrix:
        print(''.join([f'{val:>4}' for val in row]))
    print('*' * 24)
