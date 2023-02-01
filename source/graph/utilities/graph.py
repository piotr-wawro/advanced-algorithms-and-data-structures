from graph.utilities.datamodel import AdjacencyMatrix, Path
from graph.utilities.support import alpha_to_numeric, alphabet, numeric_to_alpha

class Graph(object):

    def __init__(self, size: int = 0, is_directed: bool = False) -> None:
        self.graph: AdjacencyMatrix = []
        self.is_directed = is_directed
        self.alphabet = alphabet

        for i in range(size):
            self.graph.append([None]*size)

    def add_edge(self, start: int|str, end: int|str, cost: int) -> None:
        self._validate_vertex(start)
        self._validate_vertex(end)

        if isinstance(start, str):
            start = alpha_to_numeric(start)
        if isinstance(end, str):
            end = alpha_to_numeric(end)

        if not self._fits_in_graph(start):
            self._expand_graph(start)
        if not self._fits_in_graph(end):
            self._expand_graph(end)

        self.graph[start][end] = cost
        if not self.is_directed:
            self.graph[end][start] = cost

    def path_cost(self, vertices: list[str | int]) -> float:
        start = vertices[0]
        cost = 0

        if isinstance(start, str):
            start = alpha_to_numeric(start)

        for end in vertices[1:]:
            if isinstance(end, str):
                end = alpha_to_numeric(end)
            
            if self.graph[start][end]:
                cost += self.graph[start][end]
                start = end
            else:
                raise ValueError(f'There is no path between {numeric_to_alpha(start)} and {numeric_to_alpha(end)}')

        return cost

    def _validate_vertex(self, vertex: int|str) -> None:
        if isinstance(vertex, str):
            self._validate_vertex_as_string(vertex)
        elif isinstance(vertex, int):
            self._validate_vertex_as_number(vertex)
        else:
            raise ValueError(f'Vertex name is not in string or number format. Got "{vertex}"') 

    def _validate_vertex_as_string(self, string: str) -> None:
        string = string.upper()
        char_in_alphabet = [True if c in self.alphabet else False for c in string]

        if not all(char_in_alphabet):
            raise ValueError(f'Vertex string should contain only alphabet characters. Got "{string}"')

    def _validate_vertex_as_number(self, number: int) -> None:
        if number < 0:
            raise ValueError(f'Vertex number should be a positive number. Got "{number}"')

    def _fits_in_graph(self, vertex_number: int) -> bool:
        return True if vertex_number < len(self.graph) else False

    def _expand_graph(self, size: int) -> None:
        size += 1

        for i in range(len(self.graph)):
            self.graph[i] += [None]*(size-len(self.graph[i]))

        for i in range(size-len(self.graph)):
            self.graph.append([None]*size)

    def __getitem__(self, key: tuple[int|str]|int|str) -> int | list[int]:
        if isinstance(key, tuple):
            self._validate_vertex(key[0])
            self._validate_vertex(key[1])

            v1 = key[0]
            v2 = key[1]

            if isinstance(v1, str):
                v1 = alpha_to_numeric(v1)
            if isinstance(v2, str):
                v2 = alpha_to_numeric(v2)

            return self.graph[v1][v2]

        elif isinstance(key, str):
            self._validate_vertex(key)
            key = alpha_to_numeric(key)
            return self.graph[key]

        elif isinstance(key, int):
            self._validate_vertex(key)
            return self.graph[key]

    def __len__(self):
        return len(self.graph)
