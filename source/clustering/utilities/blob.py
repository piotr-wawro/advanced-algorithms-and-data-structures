import math
import random
from clustering.utilities.datamodel import Point

def blob(center: list[float], radius: int, number_of_point: int) -> list[list[float]]:
    points: list[list[float]] = []

    for _ in range(number_of_point):
        argumenr = random.uniform(0, 360)
        modulus = random.uniform(0, radius)

        points.append([
            modulus*math.cos(argumenr) + center[0],
            modulus*math.sin(argumenr) + center[1]
        ])

    return points

def blob_uniform(center: list[float], radius: int, number_of_point: int, dim: int) -> list[list[float]]:
    points: list[list[float]] = []

    for _ in range(number_of_point):
        point = [random.uniform(center[i] - radius, center[i] + radius) for i in range(dim)]

        while sum([math.pow(point[i] - center[i], 2) for i in range(dim)]) > math.pow(radius,2):
            point = [random.uniform(center[i] - radius, center[i] + radius) for i in range(dim)]

        points.append(point)

    return points
