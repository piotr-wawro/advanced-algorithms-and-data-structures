import math
from graph.utilities.graph import Graph
from graph.utilities.datamodel import Path, Edge
from graph.utilities.support import alpha_to_numeric, numeric_to_alpha

def dijkstras_algorithm(g: Graph, start: int|str) -> list[Path]:
    if isinstance(start, str):
        start = alpha_to_numeric(start)

    vertex_edges: dict[int, list[Edge]] = {}
    for i in range(len(g)):
        vertex_edges[i] = []
        for j in range(len(g)):
            if g[i][j] != None:
                vertex_edges[i].append(Edge(start=i, end=j, cost=g[i][j]))

    paths_to_vertices: list[Path] = []
    for i in range(len(g)):
        paths_to_vertices.append(Path(path=[], cost=math.inf))
    paths_to_vertices[start].path = [numeric_to_alpha(start)]
    paths_to_vertices[start].cost = 0

    visited = []

    while len(visited) < len(g):
        vertex = get_unvisited_with_shortest_path(paths_to_vertices, visited)
        visited.append(vertex)

        for edge in vertex_edges[vertex]:
            if paths_to_vertices[edge.start].cost + edge.cost < paths_to_vertices[edge.end].cost:
                paths_to_vertices[edge.end].cost = paths_to_vertices[edge.start].cost + edge.cost
                paths_to_vertices[edge.end].path = paths_to_vertices[edge.start].path + [numeric_to_alpha(edge.end)]

    return paths_to_vertices

def get_unvisited_with_shortest_path(path_to_vertex: list[Path], visited: list[int]) -> int:
    min_val = math.inf
    min_idx = None

    for vertex_idx, vertex in enumerate(path_to_vertex):
        if vertex_idx not in visited and vertex.cost <= min_val:
            min_val = vertex.cost
            min_idx = vertex_idx

    return min_idx
