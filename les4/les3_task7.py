"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

import random
import timeit
import cProfile


# SOLUTIONS
def solution_a(items):
    res = (None, None)

    for val in items:
        if res[0] is None or res[0] > val:
            res = (val, res[1])
        elif res[1] is None or res[1] > val:
            res = (res[0], val)

    return res


def solution_b(items):
    min_a = None
    min_b = None

    _i = 0
    _len = len(items)

    while _i < _len:
        val = items[_i]
        if min_a is None or min_a > val:
            min_a = val
        elif min_b is None or min_b > val:
            min_b = val

        _i += 1

    return min_a, min_b


def solution_c(items):
    def _sorter(_items):
        if len(_items) <= 1:
            return _items

        else:
            et = [_items[0]]
            lt = []
            gt = []

            for val in _items[1:]:
                if val < et[0]:
                    lt.append(val)

                elif val > et[0]:
                    gt.append(val)

                else:
                    et.append(val)

            return _sorter(lt) + et + _sorter(gt)

    return _sorter(items)[:2]


# TESTS
def run_timeit_test(test_values):
    totals = {}

    def print_row(*args):
        print(f'{args[0]:<10} {args[1]:>10} {args[2]:>10} {args[3]:>30}')

    for func in [solution_a, solution_b, solution_c]:
        print('*' * 64)
        print(f'\nNow testing {func.__name__} (timeit)')
        print_row('LIST SIZE', 'VAL A', 'VAL B', 'TEST')

        for val in test_values:
            key = len(val)
            res = func(val)
            timeit_res = timeit.timeit(lambda: func(val), number=1000)

            totals[key] = totals[key] if key in totals else (timeit_res, func.__name__)
            totals[key] = totals[key] if timeit_res > totals[key][0] else (timeit_res, func.__name__)

            print_row(key, res[0], res[1], timeit_res)

    print('*' * 64)
    print('\nBest results')
    print_row('VALUE', 'SOLUTION', '', 'RESULT')

    for key, val in totals.items():
        print_row(key, val[1], '', val[0])


def run_cProfile_test(test_values):
    for func in [solution_a, solution_b, solution_c]:
        print(f'Now testing {func.__name__} (cProfile)\n')
        for val in test_values:
            cProfile.run(f'{func.__name__}({val})')


if __name__ == '__main__':
    is_done = False

    while not is_done:
        user_select = input(f'\n\nSelect Mode:\n[T]: timeit\n[C]: cProfile\n[Q]: quit\n>>> ').lower()

        if user_select == 't' or user_select == 'c':
            values = [[random.randint(-9999, 9999) for _ in range(0, 10 ** (i + 1))] for i in range(0, 4)]
            print('\nGenerated data: ')
            print(values)

            if user_select == 't':
                run_timeit_test(values)
            elif user_select == 'c':
                run_cProfile_test(values)

        elif user_select == 'q':
            is_done = True


# Conclusion:  after ten tests there were almost equal performance results for solutions A & B, while C is really slow

