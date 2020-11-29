"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34564, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
import timeit
import cProfile


# SOLUTIONS
def solution_a(num):
    odds = []
    evens = []

    for _val in [int(val) for val in str(num)]:
        if _val & 1:
            odds.append(_val)
        else:
            evens.append(_val)

    return num, odds, evens


def solution_b(num):
    odds = []
    evens = []

    _num = num

    while _num > 0:
        _val = _num % 10
        _num //= 10

        if _val & 1:
            odds.append(_val)
        else:
            evens.append(_val)

    return num, odds, evens


def solution_c(num):
    odds = []
    evens = []

    _num = str(num)
    _len = len(_num)
    _i = 0

    for _i in range(_len):
        _val = int(_num[_i])

        if _val & 1:
            odds.append(_val)
        else:
            evens.append(_val)

    return num, odds, evens


# TESTS
def run_timeit_test(test_values):

    totals = {}

    def print_row(*args):
        print(f'{args[0]:<10} {args[1]:>10} {args[2]:>10} {args[3]:>30}')

    for func in [solution_a, solution_b, solution_c]:
        print('*' * 64)
        print(f'\nNow testing {func.__name__} (timeit)')
        print_row('VALUE', 'ODDS', 'EVENS', 'TEST')

        for val in test_values:
            res = func(val)
            timeit_res = timeit.timeit(lambda: func(val), number=1000)

            totals[val] = totals[val] if val in totals else (timeit_res, func.__name__)
            totals[val] = totals[val] if timeit_res > totals[val][0] else (timeit_res, func.__name__)

            print_row(val, len(res[1]), len(res[2]), timeit_res)

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
    values = [123456, 364638, 31235, 997531, 264842]

    while not is_done:
        user_select = input(f'\n\nSelect Mode:\n[T]: timeit\n[C]: cProfile\n[Q]: quit\n>>> ').lower()

        if user_select == 't':
            run_timeit_test(values)
        elif user_select == 'c':
            run_cProfile_test(values)
        elif user_select == 'q':
            is_done = True


# Conclusion:  the best results occurs while using solution_b, where number splitted into parts with
# "division without reminder" algorithm.
