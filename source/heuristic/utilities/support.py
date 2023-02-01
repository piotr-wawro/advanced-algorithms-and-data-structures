import math
import random
from heuristic.utilities.canvas import Interval

def initialize_population(pop_num: int, dimension: int, interval: Interval) -> list[list[float]]:
    population: list[list[float]] = []
    for _ in range(pop_num):
        population.append([random.uniform(interval.min, interval.max)
                           for _ in range(dimension)])

    return population

def distance(a: list[float], b: list[float]):
    diff = [k-l for k, l in zip(a, b)]
    return math.hypot(*diff)

def normalization(x: float, old: Interval, new: Interval) -> float:
    return new.min + (x - old.min)/(old.max-old.min)*(new.max-new.min)
