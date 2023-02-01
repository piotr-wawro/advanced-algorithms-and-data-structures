import math
from graph.utilities.graph import Graph
from graph.utilities.datamodel import Path, Edge
from graph.utilities.support import alpha_to_numeric, numeric_to_alpha

def bellman_ford(g: Graph, start: int|str) -> list[Path]:
    if isinstance(start, str):
        start = alpha_to_numeric(start)

    edges: list[Edge] = []
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] != None:
                edges.append(Edge(start=i, end=j, cost=g[i][j]))

    paths_to_vertices: list[Path] = []
    for i in range(len(g)):
        paths_to_vertices.append(Path(path=[], cost=math.inf))
    paths_to_vertices[start].path = [numeric_to_alpha(start)]
    paths_to_vertices[start].cost = 0

    iteration = 0
    cost_updated = True

    while cost_updated:
        cost_updated = False
        iteration += 1

        if iteration > len(g) - 1:
            raise RecursionError('Graph has negative cycle')

        for edge in edges:
            if paths_to_vertices[edge.start].cost == math.inf:
                # We don't know how to get to the start_vertex
                continue

            if paths_to_vertices[edge.start].cost + edge.cost < paths_to_vertices[edge.end].cost:
                paths_to_vertices[edge.end].cost = paths_to_vertices[edge.start].cost + edge.cost
                paths_to_vertices[edge.end].path = paths_to_vertices[edge.start].path + [numeric_to_alpha(edge.end)]
                cost_updated = True

    return paths_to_vertices
