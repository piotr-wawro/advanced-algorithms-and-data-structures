from dataclasses import dataclass
from graph.utilities.support import alpha_to_numeric

@dataclass
class Path:
    path: list[str]
    cost: int

@dataclass
class VertexDegree:
    vertex: int
    degree: int

class Edge:

    def __init__(self, start: int|str, end: int|str, cost: int) -> None:
        self.start = start
        self.end = end
        self.cost = cost

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return NotImplemented

        if self.start != other.start: return False
        if self.end   != other.end:   return False
        if self.cost  != other.cost:  return False

        return True

    def __repr__(self) -> str:
        return f'Edge({self.start}, {self.end}, {self.cost})'

    @property
    def start(self) -> int:
        return self._start

    @start.setter
    def start(self, start: int|str) -> None:
        if isinstance(start, str):
            start = alpha_to_numeric(start)
        self._start = start

    @property
    def end(self) -> int:
        return self._end

    @end.setter
    def end(self, end: int|str) -> None:
        if isinstance(end, str):
            end = alpha_to_numeric(end)
        self._end = end

AdjacencyMatrix = list[list[int]]
ConnectedGraph = list[list[Path]]