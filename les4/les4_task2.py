"""
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения
простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
"""

import timeit
import cProfile


# SOLUTIONS
def solution_a(n):
    values = []
    val = 2
    _len = 0

    while _len < n:
        is_simple = True

        for _val in values:
            if not (val % _val):
                is_simple = False
                break

        if is_simple:
            values.append(val)
            _len = len(values)

        val += 1

    return values[-1]


def solution_b(n):
    values = [2]
    step = 100

    def is_simple(_val):
        if not _val % 2:
            return _val == 2

        else:
            _i = 3

            while (_i ** 2 <= _val) and (_val % _i):
                _i += 2

            return _i ** 2 > _val

    _len = len(values)

    while _len < n:
        from_val = values[-1]
        to_val = from_val + step
        for val in [val for val in range(from_val, to_val)]:
            if val > 2 and is_simple(val):
                values.append(val)
                _len = len(values)

    return values[-1]


# TESTS
def run_timeit_test(test_values):
    totals = {}

    def print_row(*args):
        print(f'{args[0]:<10} {args[1]:>10} {args[2]:>10} {args[3]:>30}')

    for func in [solution_a, solution_b]:
        print('*' * 64)
        print(f'\nNow testing {func.__name__} (timeit)')
        print_row('LIMIT', 'VALUE', '', 'TEST')

        for val in test_values:
            res = func(val)
            timeit_res = timeit.timeit(lambda: func(val), number=1000)

            totals[val] = totals[val] if val in totals else (timeit_res, func.__name__)
            totals[val] = totals[val] if timeit_res > totals[val][0] else (timeit_res, func.__name__)

            print_row(val, res, '', timeit_res)

    print('*' * 64)
    print('\nBest results')
    print_row('VALUE', 'SOLUTION', '', 'RESULT')

    for key, val in totals.items():
        print_row(key, val[1], '', val[0])


def run_cProfile_test(test_values):
    for func in [solution_a, solution_b]:
        print(f'Now testing {func.__name__} (cProfile)\n')
        for val in test_values:
            cProfile.run(f'{func.__name__}({val})')


if __name__ == '__main__':
    testable_values = [10, 50, 100, 200]

    is_done = False

    while not is_done:
        user_select = input(f'\n\nSelect Mode:\n[T]: timeit\n[C]: cProfile\n[Q]: quit\n>>> ').lower()

        if user_select == 't':
            run_timeit_test(testable_values)

        elif user_select == 'c':
            run_cProfile_test(testable_values)

        elif user_select == 'q':
            is_done = True

# Conclusion:  after ten tests there solution_a showed itself almost 2 times faster then solution_b
