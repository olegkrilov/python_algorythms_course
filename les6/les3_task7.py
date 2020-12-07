"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
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


def main():
    test_values = [[randint(-9999, 9999) for _ in range(0, 10 ** (i + 1))] for i in range(0, 4)]

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

        for val in test_values:
            memory_analyzer.reset()
            res = solution(val, memory_analyzer)
            results.append([len(val), res[0], res[1], memory_analyzer.total])

        print_results(results)


def print_results(data):
    _str = ''

    def _build_row(d):
        return f'{d[0]:<30}{d[1]:>20}{d[2]:>20}{d[3]:>30}'

    _str += _build_row(['ARRAY SIZE', 'MIN 1', 'MIN 2', 'MEMORY'])
    _str += '\n'
    _str += '-' * 100
    _str += '\n'

    for val in data:
        _str += _build_row(val)
        _str += '\n'

    print(_str)


# SOLUTIONS
def solution_a(items: [int], memory_analyzer: MemoryAnalyzer):
    res = (None, None)

    for val in items:
        if res[0] is None or res[0] > val:
            res = memory_analyzer.update((val, res[1]))
        elif res[1] is None or res[1] > val:
            res = memory_analyzer.update((res[0], val))

    return memory_analyzer.update(res)


def solution_b(items: [int], memory_analyzer: MemoryAnalyzer):
    min_a = None
    min_b = None

    _i = 0
    _len = memory_analyzer.update(len(items))

    while _i < _len:
        val = memory_analyzer.update(items[_i])
        if min_a is None or min_a > val:
            min_a = val
        elif min_b is None or min_b > val:
            min_b = val

        _i += 1

    return memory_analyzer.update(min_a, min_b)


def solution_c(items: [int], memory_analyzer: MemoryAnalyzer):
    def _sorter(_items):
        if len(_items) <= 1:
            return _items

        else:
            et = [_items[0]]
            lt = []
            gt = []

            for val in memory_analyzer.update(_items[1:]):
                if val < et[0]:
                    lt.append(val)

                elif val > et[0]:
                    gt.append(val)

                else:
                    et.append(val)

            return memory_analyzer.update(_sorter(lt) + et + _sorter(gt))

    return memory_analyzer.update(_sorter(items)[:2])


if __name__ == '__main__':
    main()

# Min memory usage could be achieved with solution_a,
# Max memory usage could be achieved with solution_c
