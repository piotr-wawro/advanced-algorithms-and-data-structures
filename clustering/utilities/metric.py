import math

def euclidean_distance(a: list[float], b: list[float]):
    diff = [k-l for k, l in zip(a, b)]
    return math.hypot(*diff)

def manhattan_distance(a: list[float], b: list[float]):
    return sum([abs(k-l) for k, l in zip(a, b)])
