"""
4. Определить, какое число в массиве встречается чаще всего.
"""

from random import randint

limits = [0, 10]
random_size = randint(10, 20)
initial_array = [randint(*limits) for _ in range(0, random_size)]
max_qty = (0, 0)
items = {}

for val in initial_array:
    items[val] = items[val] if val in items else 0
    items[val] += 1
    max_qty = max_qty if items[val] <= max_qty[1] else (val, items[val])
    # if use <= operator the stored value will be the last one, else - the first one

items = None
print(sorted(initial_array))  # Sorted used here only to better visualize result
print(max_qty)
