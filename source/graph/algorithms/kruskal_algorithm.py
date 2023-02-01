from graph.utilities.graph import Graph
from graph.utilities.datamodel import Edge
from graph.utilities.support import numeric_to_alpha

def kruskal_algorithm(g: Graph) -> list[Edge]:
    edges: list[Edge] = []
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] != None:
                edges.append(Edge(start=i, end=j, cost=g[i][j]))
    edges = sorted(edges, key=lambda edge: edge.cost)

    trees: list[list[str]] = [[numeric_to_alpha(i)] for i in range(len(g))]
    edges_of_spanning_tree: list[Edge] = []

    while len(trees) > 1:
        edge = edges.pop(0)

        start_tree = find_vertex_tree(edge.start, trees)
        end_tree = find_vertex_tree(edge.end, trees)

        if start_tree == end_tree:
            continue

        trees.remove(start_tree)
        trees.remove(end_tree)
        trees.append(start_tree + end_tree)

        edges_of_spanning_tree.append(edge)

    return edges_of_spanning_tree

def find_vertex_tree(vertex: int|str, trees: list[list[str]]) -> list[str]:
    if isinstance(vertex, int):
        vertex = numeric_to_alpha(vertex)

    for tree in trees:
        for leaf in tree:
            if vertex == leaf:
                return tree
