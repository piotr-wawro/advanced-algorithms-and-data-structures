from graph.utilities.graph import Graph
from graph.utilities.datamodel import Path
from graph.utilities.support import alpha_to_numeric, numeric_to_alpha

def travelling_salesman_nearest_neighbour(g: Graph, start: int|str) -> list[Path]:
    if isinstance(start, str):
        start = alpha_to_numeric(start)

    paths: dict[str,int] = {}

    paths_to_check: list[dict[str,]] = [{
        'path': [numeric_to_alpha(start)],
        'path_cost': 0,
        'current_vertex': start,
        'visited_vertices': [start],
    }]

    while len(paths_to_check):
        data = paths_to_check.pop()

        path = data['path']
        path_cost = data['path_cost']
        current_vertex = data['current_vertex']
        visited_vertices = data['visited_vertices']

        while len(visited_vertices) < len(g):
            nearest_neighbours = get_nearest_neighbours(g, visited_vertices, current_vertex)

            for nn in nearest_neighbours[1:]:
                paths_to_check.append({
                    'path': path + [numeric_to_alpha(nn)],
                    'path_cost': path_cost + g[current_vertex][nn],
                    'current_vertex': nn,
                    'visited_vertices': visited_vertices + [nn],
                })

            path += [numeric_to_alpha(nearest_neighbours[0])]
            path_cost += g[current_vertex][nearest_neighbours[0]]
            current_vertex = nearest_neighbours[0]
            visited_vertices.append(current_vertex)

        starting_point = visited_vertices[0]
        path += [numeric_to_alpha(starting_point)]
        path_cost += g[current_vertex][starting_point]

        paths[';'.join(path)] = path_cost

    min_v = min(paths.values())
    min_path = [Path(key.split(';'), val) for key, val in paths.items() if val == min_v]

    return min_path

def get_nearest_neighbours(graph: Graph, excluded_vertices: list[int], vertex: int) -> list[int]:
    posible_routs = [None if idx in excluded_vertices else val for idx, val in enumerate(graph[vertex])]
    minimum  = min([val for val in posible_routs if val])
    minimum_cost_routs = [idx for idx, val in enumerate(posible_routs) if val == minimum]

    return minimum_cost_routs
