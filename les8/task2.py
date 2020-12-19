"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал
список вершин, которые необходимо обойти.
"""
import os
from random import (randint, choice)
from string import ascii_uppercase


GRAPH_RANGE = (8, 13)
WEIGHT_RANGE = (1, 9)
COL_SIZE = 10


class Node:

    __index: int = 0

    def __init__(self, graph):
        self.__uid = Node.__index
        self.__graph = graph
        self.__parents = {}
        self.__children = {}
        self.__is_visited = False
        Node.__index += 1

    @property
    def uid(self):
        return self.__uid

    @property
    def is_visited(self):
        return self.__is_visited

    @is_visited.setter
    def is_visited(self, state):
        self.__is_visited = bool(state)

    def connect_as_parent(self, other, weight: int = 1):
        node, uid = self.__graph.get_normalized_node(other)

        if node and (uid != self.__uid) and (not self.has_child(uid)):
            self.__children[uid] = weight
            node.connect_as_child(self, weight)

        return self

    def connect_as_child(self, other, weight: int = 1):
        node, uid = self.__graph.get_normalized_node(other)

        if node and (uid != self.__uid) and (not self.has_parent(uid)):
            self.__parents[uid] = weight
            node.connect_as_parent(self, weight)

        return self

    def has_parent(self, uid):
        return uid in self.__parents

    def has_child(self, uid):
        return uid in self.__children

    def get_parents(self):
        return [self.__graph.get_node(uid) for uid in self.__parents.keys()]

    def get_children(self):
        return [self.__graph.get_node(uid) for uid in self.__children.keys()]

    def get_edge_weight(self, other):
        node, uid = self.__graph.get_normalized_node(other)

        if self.has_parent(uid):
            return self.__parents[uid]
        elif self.has_child(uid):
            return self.__children[uid]
        elif self.uid == uid:
            return 0
        else:
            return float('inf')


class Graph:

    def __init__(self, number_of_nodes: int = randint(*GRAPH_RANGE)):
        self.__nodes = {}
        self.__best_path = float('inf')

        for _ in range(number_of_nodes):
            node = Node(self)
            self.__nodes[node.uid] = node

    def __str__(self):
        __str = ''
        rows = [['\u2591' * COL_SIZE]]
        _len = len(self.nodes)

        def _build_row(*args):
            _row = ''

            for _str in args:
                _row += f'{_str:>{COL_SIZE}}'

            return _row

        for node in self.nodes:
            uid = node.uid
            new_row = ['-' for _ in range(_len + 1)]

            new_row[0] = f'#{uid}'
            new_row[uid + 1] = '-'

            for parent in node.get_parents():
                new_row[parent.uid + 1] = node.get_edge_weight(parent)

            rows[0].append(f'#{uid}')
            rows.append(new_row)

        for row in rows:
            __str += _build_row(*row)
            __str += '\n'

        return __str

    @property
    def nodes(self):
        return [node for node in self.__nodes.values()]

    @property
    def size(self):
        return len(self.nodes)

    def get_node(self, uid):
        return self.__nodes[uid] if uid in self.__nodes else None

    def get_normalized_node(self, node):
        _node = None

        if isinstance(node, Node):
            _node = node
        elif isinstance(node, int):
            _node = self.get_node(node)

        return _node, (_node.uid if _node is not None else None)

    def find_paths(self, from_point, to_point):
        point_a, uid_a = self.get_normalized_node(from_point)
        point_z, uid_z = self.get_normalized_node(to_point)
        paths = []

        if not point_a or not point_z:
            return None

        def _check_node(context: Graph, node: Node, path):
            node.is_visited = True
            path_weight = sum([val[1] for val in path])

            if path_weight < context.__best_path:
                for child in [child for child in node.get_children() if not child.is_visited]:
                    uid_c = child.uid
                    edge_weight = node.get_edge_weight(child)
                    path_weight_updated = path_weight + edge_weight

                    if path_weight_updated < context.__best_path:
                        if uid_c == uid_z:
                            context.__best_path = path_weight_updated
                            paths.append(path[:] + [(uid_c, edge_weight)])
                        else:
                            _check_node(context, child, path[:] + [(uid_c, edge_weight)])

        _check_node(self, point_a, [(uid_a, 0)])

        return paths

    def reset(self):
        for node in self.nodes:
            node.is_visited = False

        self.__best_path = float('inf')

        return self


def clear_screen():
    _ = os.system('cls') if os.name == 'nt' else os.system('clear')


def print_line(cols=0):
    print('-' * ((cols + 1) * COL_SIZE))


def main():
    is_done = False
    graph = Graph()
    nodes = graph.nodes

    for node in nodes:
        for i in range(int(graph.size / 2)):
            parent_node = choice(nodes)
            if node.uid != parent_node.uid:
                node.connect_as_child(parent_node, randint(*WEIGHT_RANGE))

    while not is_done:
        graph.reset()
        clear_screen()
        print('Graph Map:')
        print_line(graph.size)
        print(graph)

        point_a = int(input('Start from node #'))
        point_b = int(input('Move to node #'))

        paths = graph.find_paths(point_a, point_b)

        if not len(paths):
            print(f'\nThere are no available paths from node #{point_a} to node #{point_b}\n')

        else:
            print('\nBest paths:\n')
            best_path = None

            for index, path in enumerate(paths):
                total_weight = 0
                path_name = ascii_uppercase[index]
                path_view = f'Path {path_name}: [{point_a}]'

                for step in path[1:]:
                    path_view += f' == {step[1]}pts => [{step[0]}]'
                    total_weight += step[1]

                best_path = (path_name, total_weight) if best_path is None or best_path[1] > total_weight else best_path

                print(path_view)
                print(f'Total: {total_weight}\n')

            print_line(graph.size)
            print(f'Best path is: {best_path[0]} with {best_path[1]}pts.\n')

        is_done = input('Repeat [y/n] ? >>> ').lower() != 'y'


if __name__ == '__main__':
    main()
