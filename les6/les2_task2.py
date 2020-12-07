"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34564, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""
from sys import (getsizeof, version, platform)
from inspect import getsource
from random import randint


class MemoryAnalyzer:

    def __init__(self, func):
        self.__total = 0
        self.__func = getsource(func)

    def __str__(self):
        return f'In function {self.__func}\nTotal used memory: {self.__total}'

    @property
    def total(self):
        return self.__total

    @property
    def func(self):
        return self.__func

    def update(self, *vals):
        for val in vals:
            self.__total += getsizeof(val)

        return vals if len(vals) > 1 else vals[0]

    def reset(self):
        self.__total = 0
        return self


def print_results(data):
    _str = ''

    def _build_row(*vals):
        return f'{vals[0]:<20}{vals[1]:>30}{vals[2]:>30}{vals[3]:>20}'

    _str += _build_row('VALUE', 'EVENS', 'ODDS', 'MEMORY')
    _str += '\n'
    _str += '-' * 100
    _str += '\n'

    for val in data:
        _str += _build_row(val[0], len(val[1]), len(val[2]), val[3])
        _str += '\n'

    print(_str)


def main():
    test_numbers = [randint(1111111111, 99999999999) for _ in range(3)]

    print('-' * 100)
    print(f'Python: {version}\nSystem: {platform}')
    print('-' * 100)

    for solution in [solution_a, solution_b, solution_c]:
        memory_analyzer = MemoryAnalyzer(solution)
        results = []
        print('\n')
        print('-' * 100)
        print(f'Analyzing {solution.__name__}:')
        print('-' * 100)
        print(f'CODE:\n\n{memory_analyzer.func}')
        print('-' * 100)

        for val in test_numbers:
            memory_analyzer.reset()
            results.append(list(solution(val, memory_analyzer)) + [memory_analyzer.total])

        print_results(results)


# SOLUTIONS
def solution_a(num: int, memory_analyzer: MemoryAnalyzer):
    odds = []
    evens = []

    for _val in memory_analyzer.update([int(val) for val in str(num)]):
        if _val & 1:
            odds.append(_val)
        else:
            evens.append(_val)

    return memory_analyzer.update(num, odds, evens)


def solution_b(num: int, memory_analyzer: MemoryAnalyzer):
    odds = []
    evens = []

    _num = memory_analyzer.update(num)

    while _num > 0:
        _val = _num % 10
        _num //= 10

        if _val & 1:
            odds.append(_val)
        else:
            evens.append(_val)

    return memory_analyzer.update(num, odds, evens)


def solution_c(num: int, memory_analyzer: MemoryAnalyzer):
    odds = []
    evens = []

    _num = memory_analyzer.update(str(num))
    _len = memory_analyzer.update(len(_num))
    _i = 0

    for _i in memory_analyzer.update(range(_len)):
        _val = memory_analyzer.update(int(_num[_i]))

        if _val & 1:
            odds.append(_val)
        else:
            evens.append(_val)

    return memory_analyzer.update(num, odds, evens)


if __name__ == '__main__':
    main()

# Min memory usage could be achieved with solution_b,
# Max memory usage could be achieved with solution_c
