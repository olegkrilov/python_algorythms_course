"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import uniform


RANGE = (0, 50)
LEN = 10


def print_nums(nums, sorted_nums):
    for i in range(LEN):
        print(f'{nums[i]:<20} => {sorted_nums[i]:>20}')


def do_merge_sorting(nums):

    def _merge(left_hand, right_hand):
        sorted_nums = []
        i_l, len_l = 0, len(left_hand)
        i_r, len_r = 0, len(right_hand)

        while i_l < len_l and i_r < len_r:
            val_left, val_right = left_hand[i_l], right_hand[i_r]
            if val_left < val_right:
                sorted_nums.append(val_left)
                i_l += 1
            else:
                sorted_nums.append(val_right)
                i_r += 1

        if i_l < len_l:
            sorted_nums += left_hand[i_l:]

        if i_r < len_r:
            sorted_nums += right_hand[i_r:]

        return sorted_nums

    def _prepare(_nums):
        _len = len(_nums)

        if _len < 2:
            return _nums[:]

        else:
            base_index = int(_len / 2)
            left_hand = _prepare(_nums[:base_index])
            right_hand = _prepare(_nums[base_index:])

            return _merge(left_hand, right_hand)

    print_nums(nums, _prepare(nums))


def main():
    nums = [uniform(*RANGE) for _ in range(LEN)]
    print('\n')
    do_merge_sorting(nums)


if __name__ == '__main__':
    main()
