import random
from typing import Callable
from heuristic.utilities.canvas import Canvas, Interval, draw
from heuristic.utilities.support import distance, initialize_population, normalization

def ant_algorithm(function: Callable[[list[float]], float], dimension: int, interval: Interval, iterations: int, pop_num: int, evaporation: float, feromon_influence: float, canvas: Canvas = None):
    population: list[list[float]] = initialize_population(pop_num, dimension, interval)
    solution = [function(sample) for sample in population]

    sorted_solution, sorted_it = zip(*[[s,i] for s, i in sorted(zip(solution, range(pop_num)))])
    feromons = [1 if i in sorted_it[:round(pop_num*0.1)] else 0 for i in range(pop_num)]

    generation = 0
    while generation < iterations:
        if canvas:
            draw(canvas, interval.min, interval.max, population, 0.1)

        for i in range(pop_num):
            iter_list = list(range(pop_num))
            iter_list.remove(i)

            prob: list[float] = [0]*pop_num
            for j in iter_list:
                prob[j] = (feromons[j]/(1+distance(population[i], population[j])**2))
            prob = [normalization(p, Interval(min(prob), max(prob)), Interval(0, 1)) for p in prob]
            prob = [p/max(prob) for p in prob]

            rnd = random.random()
            for j in iter_list:
                if rnd <= prob[j]:
                    diff = [b-a for a, b in zip(population[i], population[j])]
                    population[i] = [x+d*feromon_influence for x, d in zip(population[i], diff)]
                    break

        solution = [function(sample) for sample in population]
        sorted_solution, sorted_it = zip(*[[s,i] for s, i in sorted(zip(solution, range(pop_num)))])
        feromons = [f*evaporation for f in feromons]
        feromons = [f+1 if i in sorted_it[:round(pop_num*0.1)] else f for i, f in enumerate(feromons)]
        best_sample = min(zip(solution, population))[1]

    generation += 1

    return best_sample
