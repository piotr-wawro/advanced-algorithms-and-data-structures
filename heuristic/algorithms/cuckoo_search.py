import math
import random
from typing import Callable

from heuristic.utilities.canvas import Canvas, Interval, draw
from heuristic.utilities.support import initialize_population


def cuckoo_search(function: Callable[[list[float]], float], dimension: int, interval: Interval, iterations: int, pop_num: int, detection_prob: float, canvas: Canvas = None):
    population: list[list[float]] = initialize_population(pop_num, dimension, interval)
    solution: float = [function(sample) for sample in population]

    best_solution, best_sample = min(zip(solution, population))

    generation = 0
    while generation < iterations:
        if canvas:
            draw(canvas, interval.min, interval.max, population, 0.1)

        new_best_solution, new_best_sample = min(zip(solution, population))
        if new_best_solution < best_solution:
            best_sample = new_best_sample
            best_solution = new_best_solution

        for i in range(pop_num):
            if random.random() < detection_prob:
                sample1, sample2 = random.sample(population, 2)
                population[i] = [x+random.random()*0.1*(y-z) for x, y, z in zip(population[i], sample1, sample2)]
                solution[i] = function(population[i])

            new_sample = [x + random.gauss(0, 1)*levy_flight()*(y-x)
                          for x, y in zip(population[i], best_sample)]
            new_solution = function(new_sample)

            if new_solution < solution[i]:
                population[i] = new_sample
                solution[i] = new_solution

        generation += 1

    return best_sample

def levy_flight(beta: float = 1.5) -> float:
    sigma_v = 1
    sigma_u = ((random.gammavariate(1+beta, 1)*math.sin(math.pi*beta/2))/(random.gammavariate((1+beta)/2, 1)*beta*2**((beta-1)/2)))**(1/beta)
    v = random.normalvariate(0, sigma_v)
    u = random.normalvariate(0, sigma_u)

    return u/abs(v)**(1/beta)
