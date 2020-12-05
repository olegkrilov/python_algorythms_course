"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import (namedtuple)


class CustomHex:

    __keys = {key: index for index, key in enumerate('0123456789ABCDEF')}

    __vals = {index: key for index, key in enumerate('0123456789ABCDEF')}

    def __init__(self, val='0'):
        self._val = [_val for _val in str(val).upper()]

    @property
    def val(self):
        return self._val

    @property
    def decimal(self):
        _int = 0
        _i = 0
        _len = len(self._val)
        _val = self._val[::-1]

        while _i < _len:
            _int += CustomHex.__keys[_val[_i]] * (16 ** _i)
            _i += 1

        return _int

    def __str__(self):
        return ''.join(self._val)

    def __add__(self, other):
        return CustomHex(
            CustomHex.to_hex(
                self.decimal + other.decimal
            )
        )

    def __mul__(self, other):
        return CustomHex(
            CustomHex.to_hex(
                self.decimal * other.decimal
            )
        )

    @staticmethod
    def to_hex(val):
        _res = []

        while val > 0:
            _res.append(CustomHex.__vals[val % 16])
            val //= 16

        return ''.join(_res[::-1])


def get_equation():
    props = ['a', 'action', 'b']
    Equation = namedtuple('Equation', props)

    return Equation(
        CustomHex(input('a = >>> ')),
        input('[+ or *] >>> '),
        CustomHex(input('b = >>> '))
    )


if __name__ == '__main__':
    equation = get_equation()

    if equation[1] == '+':
        print(f'{equation[0]} + {equation[2]} = {equation[0] + equation[2]}')

    elif equation[1] == '*':
        print(f'{equation[0]} * {equation[2]} = {equation[0] * equation[2]}')

    else:
        print('ERROR: Unsupported operation!')
