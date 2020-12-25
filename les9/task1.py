"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
"""
import os
from hashlib import sha1


class AwesomeSubstringsSeeker:

    def __init__(self, data: str):
        self.__data: str = data
        self.__size: int = len(data)

    def __str__(self):
        _str = ''
        iterations = {}
        substring_size = self.__size - 1

        while substring_size:
            iterations[substring_size] = self.scan_by_size(substring_size)
            substring_size -= 1

        for key, val in iterations.items():
            _str += ('-' * 100)
            _str += f'\nCheck strings with size {key}\n'
            _str += ('-' * 100)

            for _key, _val in val.items():
                _str += f'\nString value: {_val["STR"]}'
                _str += f'\n Entries qty: {_val["QTY"]}'
                _str += f'\n        Hash: {_key}\n'

        return _str

    def scan_by_size(self, size: int):
        cursor = 0
        last_index = self.__size - size
        substrings = {}

        while cursor <= last_index:
            substring = self.__data[cursor: cursor + size]
            hashed_string = AwesomeSubstringsSeeker.encode(substring)

            if hashed_string not in substrings:
                substrings[hashed_string] = {
                    'STR': substring,
                    'QTY': 0
                }

                for i in range(self.__size - size + 1):
                    substrings[hashed_string]['QTY'] += bool(
                        AwesomeSubstringsSeeker.encode(self.__data[i: i + size]) == hashed_string
                    )

            cursor += 1

        return substrings

    @classmethod
    def encode(cls, data: str, encode: str = 'utf-8'):
        return sha1(data.encode(encode)).hexdigest()


def clear_screen():
    _ = os.system('cls') if os.name == 'nt' else os.system('clear')


def main():

    is_done = False

    while not is_done:
        clear_screen()
        print(AwesomeSubstringsSeeker(input('Enter test data >>> ')))
        is_done = input('Repeat [y/n] ? >>> ').lower() != 'y'


if __name__ == '__main__':
    main()
