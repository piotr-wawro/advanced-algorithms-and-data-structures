import math
import random
from typing import Callable

from heuristic.utilities.canvas import Canvas, Interval, draw
from heuristic.utilities.support import initialize_population

def bat_algorithm(function: Callable[[list[float]], float], dimension: int, interval: Interval, iterations: int, pop_num: int, frequency: Interval, A: float, r: Interval, A_cooling_factor: float, r_cooling_factor: float, canvas: Canvas = None):
    population = initialize_population(pop_num, dimension, interval)
    velocity = initialize_population(pop_num, dimension, Interval(0,0))
    solution = [function(sample) for sample in population]
    laudness = [A for _ in range(pop_num)]
    pulse_rate = [r.max for _ in range(pop_num)]

    best_sample = min(zip(solution, population))[1]

    generation = 0
    while generation < iterations:
        if canvas:
            draw(canvas, interval.min, interval.max, population, 0.1)

        for i in range(pop_num):
            if random.random() > pulse_rate[i]:
                new_sample = best_sample
            else:
                beta = random.random()
                frequency_sample = frequency.min + (frequency.max - frequency.min) * beta
                diff = [x-y for x, y in zip(best_sample, population[i])]

                new_velocity = [v+dx*frequency_sample for v, dx in zip(velocity[i], diff)]
                new_sample = [x+v for x, v in zip(population[i], velocity[i])]

            avg_laudness = sum(laudness) / len(laudness)
            new_sample = [x+random.uniform(-1,1)*avg_laudness for x in new_sample]
            new_solution = function(new_sample)

            if random.random() < laudness[i] and new_solution < solution[i]:
                population[i] = new_sample
                velocity[i] = new_velocity
                solution[i] = new_solution
                laudness[i] *= A_cooling_factor
                pulse_rate[i] = r.min*(1-math.exp(-r_cooling_factor*generation))

        solution = [function(sample) for sample in population]
        best_sample = min(zip(solution, population))[1]

        generation += 1

    return best_sample
