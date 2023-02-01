from graph.utilities.datamodel import VertexDegree
from graph.utilities.graph import Graph

def coloring_smallest_last(graph: Graph):
    vertecies_tmp: list[VertexDegree] = []
    vertecies: list[VertexDegree] = []
    for i in range(len(graph)):
        vertecies_tmp.append(VertexDegree(i, len([e for e in graph[i] if e])))
    while len(vertecies_tmp) > 0:
        min_degree_vertex = min(vertecies_tmp, key=lambda vd: vd.degree)
        min_degree_vertex_idx = vertecies_tmp.index(min_degree_vertex)
        vertecies.append(vertecies_tmp.pop(min_degree_vertex_idx))

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
