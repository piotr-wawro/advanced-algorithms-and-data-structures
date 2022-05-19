import math
import time
from typing import Callable
import random

from heuristic.utilities.canvas import Canvas, Interval, draw

def genetic_algorithm(function: Callable[[list[float]], float], dimension: int, interval: Interval, iterations: int, pop_num: int, dropout: float, mutation_prob: float, canvas: Canvas = None):
    population: list[list[float]] = []
    for _ in range(pop_num):
        population.append([random.uniform(interval.min, interval.max)
                           for _ in range(dimension)])

    generation = 0
    while generation < iterations:
        if canvas:
            draw(canvas, interval.min, interval.max, population, 0.1)

        solution = [function(sample) for sample in population]
        population = [sample for _, sample in sorted(zip(solution, population))]
        population = population[0:math.floor(pop_num*(1-dropout))]

        if canvas:
            draw(canvas, interval.min, interval.max, population, 0.1)

        for _ in range(math.ceil(pop_num*dropout)):
            father = random.sample(population, 1)[0]
            mother = random.sample(population, 1)[0]

            child = []
            for i in range(dimension):
                if random.random() < mutation_prob:
                    child.append(random.uniform(interval.min, interval.max))
                elif random.random() < 0.5:
                    child.append(father[i])
                else:
                    child.append(mother[i])
            population.append(child)

        generation += 1

    return population[0]
