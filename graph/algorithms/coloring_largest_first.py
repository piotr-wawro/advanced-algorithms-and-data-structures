from graph.utilities.datamodel import VertexDegree
from graph.utilities.graph import Graph

def coloring_largest_first(graph: Graph):
    vertecies: list[VertexDegree] = []
    for i in range(len(graph)):
        vertecies.append(VertexDegree(i, len([e for e in graph[i] if e])))
    vertecies = sorted(vertecies, key=lambda vd: vd.degree)

    color_pool: list[set[int]] = []
    while len(vertecies) > 0:
        vertex = vertecies.pop().vertex
        connected = [vert for vert, cost in enumerate(graph[vertex]) if cost]

        for pool in color_pool:
            if any(v in pool for v in connected):
                pass
            else:
                pool.add(vertex)
                break
        else:
            color_pool.append({vertex})

    return color_pool
