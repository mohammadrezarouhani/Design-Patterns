from typing import Dict


class Node:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()


class Graph:
    nodes: Dict[str, Node] = {}

    def add_node(self, node: Node):
        if type(node) == Node and node.name not in self.nodes:
            self.add_node[node.name] = node
            return True
        else:
            return False

    def add_edge(self, start_node, end_node):
        if start_node in self.nodes and end_node in self.nodes:
            for key, value in self.nodes.items():
                if key == start_node:
                    value.add_neighbor(end_node)
                if key == end_node:
                    value.add_neighbor(start_node)
        else:
            return False

