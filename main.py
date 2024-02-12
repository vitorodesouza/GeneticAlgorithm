from genetic.genetic.chromosome import Chromosome
from genetic.genetic.gene import Gene
from genetic.genetic.genetic import Genetic
from genetic.genetic.crossovers import ArithimeticCrossover, SinglePointCrossover
from genetic.genetic.individual import Individual
from genetic.genetic.mutations import UniformMutation
from genetic.genetic.population import Population
from genetic.genetic.selections import RouletteSelection, RandomSelection
from genetic.genetic.problems import AckleyProblem, MaxZero
import matplotlib.pyplot as plt
import random

from genetic.utils import plot_history

if __name__ == "__main__":

    population_size = 10
    mutation_rate = 1
    generations = 400
    crossover_rate = 1
    problem = AckleyProblem(
        genes_boundries=[(-5, 5), (-5, 5)], mutation=UniformMutation(1)
    )

    ga = Genetic(
        population_size=population_size,
        mutation_rate=mutation_rate,
        generations=generations,
        crossover_rate=crossover_rate,
        problem=problem,
        crossover=ArithimeticCrossover(),
        selection=RouletteSelection(),
        verbose=1,
    )

    history, best_individual = ga.run()

    print("Best solution: ", best_individual.get_fitness())
    plot_history(history)