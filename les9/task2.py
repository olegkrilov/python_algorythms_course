"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
import os


class IncredibleHuffmanTreeItem:

    __index = 0

    __Items = []

    def __init__(self):
        self.__uid = IncredibleHuffmanTreeItem.__index
        self.__parent = None
        self.__stamp = ''
        IncredibleHuffmanTreeItem.__index += 1
        IncredibleHuffmanTreeItem.__Items.append(self)

    def set_parent(self, item=None, stamp=''):
        self.__parent = item
        self.__stamp = stamp
        return self

    @property
    def uid(self):
        return self.__uid

    @property
    def level(self):
        return (self.__parent.level + 1) if (self.__parent is not None) else 0

    @property
    def stamp(self):
        return (self.__parent.stamp if (self.__parent is not None) else '') + self.__stamp

    @property
    def items(self):
        return [item for item in IncredibleHuffmanTreeItem.__Items[:] if item.uid != self.uid]


class IncredibleHuffmanTreeLeaf(IncredibleHuffmanTreeItem):

    def __init__(self, char, weight):
        IncredibleHuffmanTreeItem.__init__(self)
        self.__char = char
        self.__weight = weight

    def __str__(self):
        return f'{self.__char} ({self.__weight})'

    @property
    def char(self):
        return self.__char

    @property
    def weight(self):
        return self.__weight


class IncredibleHuffmanTreeNode(IncredibleHuffmanTreeItem):

    def __init__(self, left_hand=None, right_hand=None):
        IncredibleHuffmanTreeItem.__init__(self)
        self.__left_hand = left_hand
        self.__right_hand = right_hand

        for index, item in enumerate([self.__left_hand, self.__right_hand]):
            if isinstance(item, IncredibleHuffmanTreeNode) or isinstance(item, IncredibleHuffmanTreeLeaf):
                item.set_parent(self, f'{index}')

    def get_child(self, n):
        return self.__left_hand if n == '0' else self.__right_hand

    @property
    def weight(self):
        weight = 0

        for item in [self.__left_hand, self.__right_hand]:
            if isinstance(item, IncredibleHuffmanTreeNode) or isinstance(item, IncredibleHuffmanTreeLeaf):
                weight += item.weight

        return weight


class IncredibleHuffmanTree:

    def __init__(self, data: str):
        self.__leaves = IncredibleHuffmanTree.__get_leaves(data)
        self.__root = IncredibleHuffmanTree.__build_tree(self.__leaves)
        self.__encoded = IncredibleHuffmanTree.__encode(self.__leaves, data)

        print(data)

    def __str__(self):
        return self.encoded

    @property
    def leaves(self):
        return sorted(self.__leaves, key=lambda d: int(d.stamp))

    @property
    def encoded(self):
        return self.__encoded

    @property
    def table(self):
        _str = f'{"CHAR:":<10}    {"CODE:"}\n'

        for leaf in self.leaves:
            char = f'{leaf.char} ({leaf.weight})'
            _str += f'{char:<10} => {leaf.stamp}\n'

        return _str

    @property
    def decoded(self):
        return IncredibleHuffmanTree.__decode(self.__leaves, self.__encoded)

    @staticmethod
    def __get_leaves(data):
        leaves = {}

        for char in data:
            leaves[char] = leaves[char] if char in leaves else 0
            leaves[char] += 1

        return sorted([IncredibleHuffmanTreeLeaf(key, val) for key, val in leaves.items()], key=lambda d: d.weight)

    @staticmethod
    def __build_tree(leaves: [IncredibleHuffmanTreeLeaf]):
        stack = leaves[:]

        while len(stack) > 1:
            node = IncredibleHuffmanTreeNode(stack[0], stack[1])
            del stack[:2]
            stack.append(node)
            stack.sort(key=lambda d: d.weight)

        return stack[0]

    @staticmethod
    def __encode(leaves, data):
        dictionary = {leaf.char: leaf.stamp for leaf in leaves}
        return ''.join([dictionary[char] for char in data])

    @staticmethod
    def __decode(leaves, data):
        dictionary = {leaf.stamp: leaf.char for leaf in leaves}
        stamp = ''
        _str = ''

        for symbol in data:
            stamp += symbol

            if stamp in dictionary:
                _str += dictionary[stamp]
                stamp = ''

        return _str


def clear_screen():
    _ = os.system('cls') if os.name == 'nt' else os.system('clear')


def main():
    is_done = False

    while not is_done:
        clear_screen()
        user_input = input('Input some text to test Huffman Algorithm >>> ')
        huffman_tree = IncredibleHuffmanTree(user_input)

        print(f'\nOriginal string: ')
        print(user_input)
        print(f'\nEncoded string: ')
        print(huffman_tree.encoded)
        print('\nTable representation: ')
        print(huffman_tree.table)
        print('\nDecoded string: ')
        print(huffman_tree.decoded)
        print('\nCompare original with decoded: ')
        print(huffman_tree.decoded == user_input)

        is_done = input('\nRepeat [y/n] ? >>> ').lower() != 'y'


if __name__ == '__main__':
    main()
