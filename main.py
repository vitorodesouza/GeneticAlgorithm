from src.genetic.genetic import Genetic
from src.genetic.crossovers import ArithimeticCrossover
from src.genetic.mutations import UniformMutation
from src.genetic.selections import RouletteSelection
from src.genetic.problems import AckleyProblem
from src.genetic.utils.utils import plot_history

if __name__ == "__main__":

    population_size = 10
    mutation_rate = 1
    generations = 400
    crossover_rate = 1
    problem = AckleyProblem(
        genes_boundaries=[(-5, 5), (-5, 5)], mutation=UniformMutation(mutation_rate=1,mutation_value=0.15)
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