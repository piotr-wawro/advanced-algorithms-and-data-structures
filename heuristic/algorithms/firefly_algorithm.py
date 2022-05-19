import math
import random
from typing import Callable
from heuristic.utilities.canvas import Canvas, Interval, draw
from heuristic.utilities.support import distance, initialize_population

def firefly_algorithm(function: Callable[[list[float]], float], dimension: int, interval: Interval, iterations: int, pop_num: int, attractiveness: float, light_absorption: float, randomness: float, canvas: Canvas = None):
    population: list[list[float]] = initialize_population(pop_num, dimension, interval)
    solution: float = [function(sample) for sample in population]

    generation = 0
    while generation < iterations:
        if canvas:
            draw(canvas, interval.min, interval.max, population, 0.1)

        for i in list(range(pop_num)):
            for j in list(range(pop_num)):
                if solution[i] > solution[j]:
                    dist = distance(population[i], population[j])
                    new_sample = [x + attractiveness*math.exp(-light_absorption*dist**2)*(y-x)+randomness*(random.random() - 0.5)
                                  for x, y in zip(population[i], population[j])]
                    new_solution = function(new_sample)

                    if new_solution < solution[i]:
                        population[i] = new_sample
                        solution[i] = new_solution

        generation += 1

    best_solution, best_sample = min(zip(solution, population))

    return best_sample
