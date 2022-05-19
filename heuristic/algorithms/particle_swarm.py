import random
from typing import Callable

from heuristic.utilities.canvas import Canvas, Interval, draw
from heuristic.utilities.support import initialize_population


def particle_swarm(function: Callable[[list[float]], float], dimension: int, interval: Interval, iterations: int, pop_num: int, corelation_to_iter: float, corelation_to_best: float, canvas: Canvas = None):
    popultaion = initialize_population(pop_num, dimension, interval)
    velocities = initialize_population(pop_num, dimension, Interval(-1,1))

    generation = 0
    best_sample_ever: list[float] = popultaion[0]
    best_sample_iter: list[float] = popultaion[0]
    while generation < iterations:
        if canvas:
            draw(canvas, interval.min, interval.max, popultaion, 0.1)

        solution = [function(sample) for sample in popultaion]
        best_sample_iter = min(zip(solution, popultaion))[1]

        if function(best_sample_iter) < function(best_sample_ever):
            best_sample_ever = best_sample_iter

        for sample, velocity in zip(popultaion, velocities):
            for i in range(dimension):
                alpha = random.random()
                beta = random.random()

                velocity[i] = corelation_to_iter*alpha*(best_sample_iter[i]-sample[i]) + corelation_to_best*beta*(best_sample_ever[i]-sample[i])
                sample[i] += beta*velocity[i]

        generation += 1

    solution = [function(sample) for sample in popultaion]
    best_sample_iter = min(zip(solution, popultaion))[1]

    if best_sample_iter < best_sample_ever:
        best_sample_ever = best_sample_iter

    return best_sample_ever