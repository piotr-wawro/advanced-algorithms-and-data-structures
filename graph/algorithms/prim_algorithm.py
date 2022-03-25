from graph.utilities.graph import Graph
from graph.utilities.datamodel import Edge

def prim_algorithm(g: Graph) -> list[Edge]:
    edges_to_vertivies: list[Edge] = [None] * len(g)
    edges_of_spanning_tree: list[Edge] = []
    connected_vertices: list[str] = []

    for i in range(len(g)):
        if g[0][i] != None:
            # Stores shortest known edge to vertex
            edges_to_vertivies[i] = Edge(start=0, end=i, cost=g[0][i])
    connected_vertices.append(0)

    while len(connected_vertices) < len(g):
        potential_edges = [edge for edge in edges_to_vertivies if edge and edge.end not in connected_vertices]
        minimum_cost_edge = min(potential_edges, key=lambda edge: edge.cost)

        edges_of_spanning_tree.append(minimum_cost_edge)
        connected_vertices.append(minimum_cost_edge.end)

        for i in range(len(g)):
            if g[minimum_cost_edge.end][i] != None:
                if edges_to_vertivies[i] == None:
                    edges_to_vertivies[i] = Edge(start=minimum_cost_edge.end, end=i, cost=g[minimum_cost_edge.end][i])
                elif g[minimum_cost_edge.end][i] < edges_to_vertivies[i].cost:
                    edges_to_vertivies[i] = Edge(start=minimum_cost_edge.end, end=i, cost=g[minimum_cost_edge.end][i])

    return edges_of_spanning_tree
