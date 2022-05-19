import collections
from typing import Callable

def KNN(points: list[list[float]], labels: int, k: int, unknown_point: list[float], metric: Callable[[list[float], list[float]], list[float]]) -> int:
    distances = [metric(unknown_point, point) for point in points]
    sorted_labels = [label for _, label in sorted(zip(distances, labels))]

    return collections.Counter(sorted_labels[:k]).most_common(1)[0][0]
