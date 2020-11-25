"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо
заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint

random_size = randint(10, 20)
first_array = [randint(0, 20) for _ in range(0, random_size)]
second_array = []

for i in range(0, random_size):
    if not (first_array[i] & 1):
        second_array.append(i)

print(first_array)
print(second_array)

