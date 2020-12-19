"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
"""
import os
from random import randint, choice, shuffle
from string import ascii_uppercase

GRAPH_SIZE = (15, 20)


class Node:

    def __init__(self, uid, graph):
        self.__uid = uid
        self.__graph = graph
        self.__children = {}
        self.__is_visited = False

    def __str__(self):
        _str = f'{self.uid} => '
        _child_nodes = ''

        for uid in self.__children.keys():
            child = self.__graph.get_node(uid)
            if not child.is_visited:
                _child_nodes += f'{uid} '

        return _str + _child_nodes if len(_child_nodes) else '-'

    def add_child(self, uid, weight: int = 1):
        if self.uid != uid and uid not in self.__children:
            self.__children[uid] = weight

    def get_child(self, uid):
        return self.__graph.get_node(uid) if uid in self.__children else None

    def get_children(self, pristine: bool = True):
        children = []

        for uid in self.__children.keys():
            child = self.get_child(uid)

            if pristine:
                if not child.is_visited:
                    children.append(child)
            else:
                children.append(child)

        return children

    @property
    def uid(self):
        return self.__uid

    @property
    def is_visited(self):
        return self.__is_visited

    @is_visited.setter
    def is_visited(self, value):
        self.__is_visited = bool(value)


class Graph:

    def __init__(self, number_of_nodes: int = randint(*GRAPH_SIZE)):
        self.__nodes = {ascii_uppercase[i]: Node(ascii_uppercase[i], self) for i in range(number_of_nodes)}
        self.__visited_nodes = {}

    def __str__(self):
        _str = 'Graph connections representation\n'

        for node in self.nodes:
            _str += f'{node}\n'

        return _str

    def get_node(self, uid):
        return self.__nodes[uid] if uid in self.__nodes else None

    def set_connections(self):
        nodes = self.nodes
        size = self.size
        shuffle(nodes)

        for index, node in enumerate(nodes):

            # This should be done to ensure every node is connected to a single line
            uid_c = nodes[0].uid if (index + 1 == size) else nodes[index + 1].uid
            node.add_child(uid_c)

            # This is just to add random connections to every node
            for _ in range(randint(0, int(size / 2))):
                node.add_child(choice(nodes).uid)

        return self

    def reset_nodes(self):
        for node in self.nodes:
            node.is_visited = False

    def get_unvisited_nodes(self):
        nodes = []
        for node in self.nodes:
            if not node.is_visited:
                nodes.append(node)

        return nodes

    @property
    def nodes(self):
        return [node for node in self.__nodes.values()]

    @property
    def size(self):
        return len(self.nodes)


class Path:

    error_message: str = 'Can\'t build path from'

    def __init__(self, node_name: str, graph: Graph):
        self.__node = node_name
        self.__graph = graph

    def __str__(self):
        start_node: Node = self.__graph.get_node(self.__node)

        if start_node is None:
            return f'\n{Path.error_message} {self.__node}'

        journey_map = {}
        forks = {}

        def _to_string():
            _str = ''

            for key in journey_map.keys():
                _str += (f'{key}: ' + ''.join([f'{node} => ' for node in journey_map[key]]) + 'DEAD END\n')

            _str += f'Nodes remain unvisited: {len(self.__graph.get_unvisited_nodes())}\n'

            return _str

        def _find_fork():
            fork = None
            uids = [key for key in forks.keys()]
            size = len(uids) - 1
            i = 0

            while fork is None or i < size:
                uid = uids[i]
                node: Node = self.__graph.get_node(uid)
                children = node.get_children()
                i += 1

                if len(children):
                    fork = node

                else:
                    del forks[uid]

            return fork

        def _explore_node(node: Node = start_node, path: str = 'MAIN '):
            journey_map[path] = journey_map[path] if path in journey_map else []
            journey_map[path].append(node.uid)

            node.is_visited = True
            children = node.get_children()
            size = len(children)

            if size:
                if size > 1:
                    forks[node.uid] = True

                _explore_node(choice(children), path)

            else:
                nodes_remain = self.__graph.get_unvisited_nodes()

                if len(nodes_remain):
                    fork = _find_fork()

                    if fork:
                        _explore_node(fork, f'FORK {fork.uid}')

        _explore_node()
        return _to_string()


def clear_screen():
    _ = os.system('cls') if os.name == 'nt' else os.system('clear')


def print_line():
    print('-' * 100)


def main():
    is_done = False
    graph = Graph().set_connections()

    while not is_done:
        graph.reset_nodes()
        clear_screen()
        print_line()
        print(graph)
        print_line()

        path = Path(
            input('Input node name you want to start from >>> ').upper(),
            graph
        )

        print_line()
        print(f'\n{path}\n')

        is_done = input('Repeat [y/n] ? >>> ').lower() != 'y'


if __name__ == '__main__':
    main()
