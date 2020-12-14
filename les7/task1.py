"""
1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
"""
from random import randint


RANGE = (-999, 999)
LEN = 10


def print_nums(nums, updates):
    print(''.join([f'{val:>10}' for val in nums]) + f'{updates:>15}')


def do_bubble_sorting(shuffled_nums):
    _is_ready = False
    _len = len(shuffled_nums)
    _i = 0

    while not _is_ready and _i < LEN:
        _updates = 0
        _ii = 0

        while _ii < (LEN - 1):
            curr_val = shuffled_nums[_ii]
            next_val = shuffled_nums[_ii + 1]

            if curr_val < next_val:
                _updates, shuffled_nums[_ii], shuffled_nums[_ii + 1] = (_updates + 1), next_val, curr_val

            _ii += 1

        if not _updates:
            _is_ready = True

        print_nums(shuffled_nums, f'<= {_updates} =>')
        _i += 1


def main():
    nums = [randint(*RANGE) for _ in range(LEN)]

    print('-' * 115)
    print_nums(nums, 'Initial')
    print('-' * 115)

    do_bubble_sorting(nums)


if __name__ == '__main__':
    main()

