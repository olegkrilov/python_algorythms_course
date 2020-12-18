"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

NAMES = [
    'Vasya',
    'Petya',
    'Kolya',
    'Fedya',
    'Misha',
    'Vadik',
    'Georg',
    'Pavel',
    'Taras',
    'Borya'
]


class Person:

    __index: int = 0

    __entities: dict = {}

    def __init__(self, name: str):
        uid = Person.__index

        self.__uid = uid
        self.__name = name
        self.__connections = {}

        Person.__index += 1
        Person.__entities[self.__uid] = self

    def shake_hand(self, other):
        _other: Person or None = None

        if isinstance(other, Person):
            _other = other
        elif isinstance(other, int) and other in Person.__entities:
            _other = Person.__entities[other]

        if _other is not None:
            self.add_relation(_other.uid)
            _other.add_relation(self.uid)
            return 1
        else:
            return 0

    def add_relation(self, uid, value=1):
        if uid not in self.__connections:
            self.__connections[uid] = value

        return self

    def get_friends(self):
        uid = self.uid
        return [Person.__entities[key] for key in Person.__entities.keys() if key != uid]

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name


def build_graph(persons: [Person]):
    total_links = 0
    rows = [['\u2591' * 10]]
    _len = len(persons)

    def _print_row(*args):
        _row = ''

        for _str in args:
            _row += f'{_str:>10}'

        print(_row)

    def _print_line():
        print('-' * (10 * (_len + 1)))

    for person in persons:
        uid, name = person.uid, person.name
        new_row = [None for _ in range(_len + 1)]

        new_row[0] = name
        new_row[uid + 1] = 0

        for friend in person.get_friends():
            total_links += person.shake_hand(friend)
            new_row[friend.uid + 1] = 1

        rows[0].append(name)
        rows.append(new_row)

    print('\n')

    for index, row in enumerate(rows):
        _print_row(*row)
        if not index:
            _print_line()

    _print_line()
    print(f'Total Links: {total_links}')

    return total_links


def main():
    number_of_persons = int(input('How many friends met [3 - 10]? >>> '))
    total_links = build_graph([Person(NAMES[i]) for i in range(number_of_persons)])

    # Test result
    assert total_links == ((number_of_persons ** 2) - number_of_persons), 'Something went wrong'


if __name__ == '__main__':
    main()

