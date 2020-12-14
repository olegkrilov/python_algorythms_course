"""
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найти в массиве медиану – элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой – не больше медианы.

Примечание: Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках.
"""

from random import randint

RANGE = (-10, 10)
LEN_A = 5
LEN_B = 9
LEN_C = 13


def calculate_median(nums):

    def get_sum(_nums):
        _sum = 0
        for _num in _nums:
            _sum += _num

        return _sum

    def get_range(_nums):
        _min_val = None
        _max_val = None

        for _num in _nums:
            _min_val = _num if _min_val is None or _min_val > _num else _min_val
            _max_val = _num if _max_val is None or _max_val < _num else _max_val

        return _min_val, _max_val

    def get_indexes(_nums, _num):
        return [i for i, _val in enumerate(_nums) if _val == _num]

    def normalize_lists(list_a, list_b, delta, val):
        indexes = get_indexes(list_a, val)[:delta]
        return [val for i, val in enumerate(list_a) if i not in indexes], list_b + [val for _ in indexes]

    nums_len = len(nums)
    required_list_size = int(nums_len / 2)

    # First step: get total sum & average
    nums_sum = get_sum(nums)
    average = nums_sum / nums_len

    # Second step: divide values onto two lists
    less_values = []
    greater_values = []

    for num in nums:
        (less_values if num < average else greater_values).append(num)

    # Third step: normalize lists
    less_values_len = len(less_values)
    greater_values_len = len(greater_values)

    if required_list_size < less_values_len:
        while len(greater_values) < required_list_size:
            less_values, greater_values = normalize_lists(
                less_values,
                greater_values,
                required_list_size - len(greater_values),
                get_range(less_values)[1]
            )

    elif required_list_size < greater_values_len:
        while len(less_values) < required_list_size:
            greater_values, less_values = normalize_lists(
                greater_values,
                less_values,
                required_list_size - len(less_values),
                get_range(greater_values)[0]
            )

    # Fourth step: define median
    median = None

    if len(less_values) > required_list_size:
        median = get_range(less_values)[1]
        less_values.remove(median)

    elif len(greater_values) > required_list_size:
        median = get_range(greater_values)[0]
        greater_values.remove(median)

    return median, less_values, greater_values


def print_results(nums, median, nums_before, nums_after):

    def _print_row(*args):
        print(f'{args[0]:>30}{args[1]:>30}{args[2]:>30}{args[3]:>30}')

    lim = len(nums_before)

    _print_row('Initial List', 'Less then Median', 'Greater then Median', 'Median Itself')

    for i, num in enumerate(nums):
        _print_row(
            f'{num}',
            f'{nums_before[i] if i < lim else ""}',
            f'{nums_after[i] if i < lim else ""}',
            f'{median if not i else ""}'
        )


def main():
    for _len in [LEN_A, LEN_B, LEN_C]:
        __len = (_len * 2) + 1
        print(f'\nGenerating data of size [ 2 * {_len} + 1 = {__len} ] in range [ {RANGE[0]}, {RANGE[1]} ]')
        nums = [randint(*RANGE) for _ in range(__len)]
        print('Now finding median')
        print('-' * 120)
        print_results(nums, *calculate_median(nums))
        print('-' * 120)


if __name__ == '__main__':
    main()

