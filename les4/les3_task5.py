"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random
import timeit
import cProfile


# SOLUTIONS
def solution_a(items):
    min_val = 0

    for val in items:
        if val < 0:
            if not min_val:
                min_val = val
            else:
                min_val = val if val > min_val else min_val

    return min_val if min_val < 0 else None


def solution_b(items):
    min_val = 0

    for val in [val for val in items if val < 0]:
        min_val = val if not min_val or val > min_val else min_val

    return min_val if min_val < 0 else None


def solution_c(items):
    min_val = 0

    _i = 0
    _len = len(items)
    while _i < _len:
        val = items[_i]
        if val < 0:
            min_val = val if not min_val or val > min_val else min_val
        _i += 1

    return min_val if min_val < 0 else None


# TESTS
def run_timeit_test(test_values):
    totals = {}

    def print_row(*args):
        print(f'{args[0]:<10} {args[1]:>10} {args[2]:>10} {args[3]:>30}')

    for func in [solution_a, solution_b, solution_c]:
        print('*' * 64)
        print(f'\nNow testing {func.__name__} (timeit)')
        print_row('LIST SIZE', 'VALUE', '', 'TEST')

        for val in test_values:
            key = len(val)
            res = func(val)
            timeit_res = timeit.timeit(lambda: func(val), number=1000)

            totals[key] = totals[key] if key in totals else (timeit_res, func.__name__)
            totals[key] = totals[key] if timeit_res > totals[key][0] else (timeit_res, func.__name__)

            print_row(key, res, '', timeit_res)

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
            values = [[random.randint(-9999, 9999) for _ in range(0, 10 ** (i + 1))] for i in range(0, 3)]
            print('\nGenerated data: ')
            print(values)

            if user_select == 't':
                run_timeit_test(values)
            elif user_select == 'c':
                run_cProfile_test(values)

        elif user_select == 'q':
            is_done = True

# Conclusion:  solution A seems is the fastest
