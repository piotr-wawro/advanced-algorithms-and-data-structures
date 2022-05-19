import random
from typing import Callable
from heuristic.utilities.canvas import Canvas, Interval, draw


def differential_evolution(function: Callable[[list[float]], float], dimension: int, interval: Interval, iterations: int, pop_num: int, cross_prob: float, mutation_var: float, canvas: Canvas = None):
    population: list[list[float]] = []
    for _ in range(pop_num):
        population.append([random.uniform(interval.min, interval.max)
                           for _ in range(dimension)])

    generation = 0
    while generation < iterations:
        if canvas:
            draw(canvas, interval.min, interval.max, population, 0.1)

        new_population = []
        for idx, sample in enumerate(population):
            k, l, m = random.sample([i for i in range(0, pop_num) if i != idx], 3)

            mutation: list[float] = []
            for i in range(dimension):
                mutation.append(population[k][i]+mutation_var*(population[l][i]-population[m][i]))

            new_sample = []
            for i in range(dimension):
                if random.random() < cross_prob:
                    new_sample.append(mutation[i])
                else:
                    new_sample.append(sample[i])

            if function(new_sample) < function(sample):
                new_population.append(new_sample)
            else:
                new_population.append(sample)

        population = new_population
        generation += 1

    solution = [function(sample) for sample in population]
    population = [sample for _, sample in sorted(zip(solution, population))]
    return population[0]
