import random
from typing import Callable
from heuristic.utilities.canvas import Canvas, Interval, draw
from heuristic.utilities.support import initialize_population

def bee_algorithm(function: Callable[[list[float]], float], dimension: int, interval: Interval, iterations: int, pop_num: int, trial_limit: int, canvas: Canvas = None):
    def update(i):
        filtered_list = [j for j in range(pop_num) if j != i]
        partner = population[random.sample(filtered_list, 1)[0]]
        idx = random.randrange(0, dimension)
        phi = random.uniform(-1,1)

        new_sample = population[i].copy()
        new_sample[idx] += phi*(new_sample[idx]-partner[idx])
        new_solution = function(new_sample)

        if new_solution < solution[i]:
            population[i] = new_sample
            solution[i] = new_solution
            fit[i] = fit_f(new_solution)
            trial[i] = 0
        else:
            trial[i] += 1

    def fit_f(solution: float) -> float:
        if solution <= 0:
            return 1/(1+abs(solution))
        else:
            return 1+abs(solution)

    population: list[list[float]] = initialize_population(pop_num, dimension, interval)
    solution: list[float] = [function(sample) for sample in population]
    fit: list[float] = [fit_f(s) for s in solution]
    trial: list[int] = [0]*pop_num

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
            if trial[i] > trial_limit:
                population[i] = initialize_population(1, dimension, interval)[0]
                solution[i] = function(population[i])
                trial[i] = 0

        for i in range(pop_num):
            update(i)

        prob: list[float] = [f/max(fit) for f in fit]

        i = 0
        for update_it in range(pop_num):
            while not random.random() < prob[i]:
                i = (i+1)%pop_num
            update(i)
            i = (i+1)%pop_num

        generation += 1

    return best_sample
