"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия. Программа должна определить среднюю
прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""
from collections import (namedtuple, defaultdict, Counter)


MONTH_KEYS = ['first', 'second', 'third', 'fourth']
YEAR_KEY = 'year'
WINNERS_KEY = 'winners'
LOSERS_KEY = 'losers'


def create_company(_id):
    props = ['id', 'name', 'profit']
    Company = namedtuple('Company', props)

    print(f'\nCompany #{_id}')
    return Company(
        _id,
        input('Company name (str) >>> '),
        Counter({key: float(input(f'{str(key).upper()} quarter profit (float) >>> ')) for key in MONTH_KEYS})
    )


def show_companies(data):
    total = Counter()
    ranks = defaultdict()
    number_of_companies = len(data) or 1

    def _print_separator(symbol='-', size=80):
        print(symbol * size)

    def _print_row(*args):
        print(f'{args[0]:<10}{args[1]:<20}{args[2]:>10}{args[3]:>10}{args[4]:>10}{args[5]:>10}{args[6]:>10}')

    # main table
    print('\n\n')
    _print_separator()
    _print_row('ID', 'Company', *[str(key).upper() for key in MONTH_KEYS], YEAR_KEY.upper())

    for d in data:
        values = [d[2][key] for key in MONTH_KEYS]
        d[2][YEAR_KEY] = sum(values)
        total += d[2]

        _print_row(f'#{d[0]}', d[1], *['{:.2f}'.format(val) for val in values], '{:.2f}'.format(d[2][YEAR_KEY]))

    year_average = total[YEAR_KEY] / number_of_companies

    _print_separator()
    _print_row('Average:', '',
               *['{:.2f}'.format((total[key] / number_of_companies)) for key in MONTH_KEYS],
               '{:.2f}'.format(year_average))
    _print_row('Total:', '', *['{:.2f}'.format(total[key]) for key in MONTH_KEYS], '{:.2f}'.format(total[YEAR_KEY]))

    # additional table
    _print_separator()

    for d in data:
        key = WINNERS_KEY if d[2][YEAR_KEY] >= year_average else LOSERS_KEY
        ranks[key] = ranks[key] if key in ranks else []
        ranks[key].append(d[1])

    for key, items in ranks.items():
        print(f'\n{key.upper()}:')
        print(*[f'{item}' for item in items], sep='\n')


if __name__ == '__main__':
    n = int(input('Number of Companies (int)     >>> '))
    companies = [create_company(i + 1) for i in range(0, n)]

    show_companies(companies)
