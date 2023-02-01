import math
from graph.algorithms.dijkstras_algorithm import dijkstras_algorithm
from graph.utilities.datamodel import ConnectedGraph
from graph.utilities.graph import Graph
from graph.algorithms.bellman_ford import bellman_ford
import copy

def johnsons_algorith(g: Graph) -> ConnectedGraph:
    g_copy = copy.deepcopy(g)

    last_vertex = len(g_copy)
    for i in range(last_vertex):
        g_copy.add_edge(last_vertex, i, 0)

    paths = bellman_ford(g_copy, last_vertex)

    g_new_weights = copy.deepcopy(g)
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] != None:
                new_weight = g[i][j] + paths[i].cost - paths[j].cost
                g_new_weights.add_edge(i, j, new_weight)

    return g_new_weights

    # pcg: ConnectedGraph = []
    # for i in range(len(g_new_weights)):
    #     pcg.append(dijkstras_algorithm(g_new_weights, i))

    # for i in range(len(pcg)):
    #     for j in range(len(pcg)):
    #         if pcg[i][j].cost != math.inf:
    #             pcg[i][j].cost = g.path_cost(pcg[i][j].path)

    # return pcg
