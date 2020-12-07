"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
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
    test_values = [[randint(-9999, 9999) for _ in range(0, 10 ** (i + 1))] for i in range(0, 3)]

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
            results.append([len(val), solution(val, memory_analyzer), memory_analyzer.total])

        print_results(results)


def print_results(data):
    _str = ''

    def _build_row(d):
        return f'{d[0]:<30}{d[1]:>30}{d[2]:>30}'

    _str += _build_row(['ARRAY SIZE', 'VALUE', 'MEMORY'])
    _str += '\n'
    _str += '-' * 100
    _str += '\n'

    for val in data:
        _str += _build_row(val)
        _str += '\n'

    print(_str)


# SOLUTIONS
def solution_a(items: [int], memory_analyzer: MemoryAnalyzer):
    min_val = 0

    for val in items:
        if val < 0:
            if not min_val:
                min_val = val
            else:
                min_val = val if val > min_val else min_val

    return memory_analyzer.update(min_val if min_val < 0 else None)


def solution_b(items: [int], memory_analyzer: MemoryAnalyzer):
    min_val = 0

    for val in memory_analyzer.update([val for val in items if val < 0]):
        min_val = val if not min_val or val > min_val else min_val

    return memory_analyzer.update(min_val if min_val < 0 else None)


def solution_c(items: [int], memory_analyzer: MemoryAnalyzer):
    min_val = 0

    _i = 0
    _len = memory_analyzer.update(len(items))
    while _i < _len:
        val = items[_i]
        if val < 0:
            min_val = val if not min_val or val > min_val else min_val
        _i += 1

    return memory_analyzer.update(min_val if min_val < 0 else None)


if __name__ == '__main__':
    main()

# Min memory usage could be achieved with solution_a,
# Max memory usage could be achieved with solution_b
