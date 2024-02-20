from .genetic import Genetic
from .crossovers import ArithimeticCrossover
from .mutations import UniformMutation
from .selections import RouletteSelection
from .problems import AckleyProblem
from .utils.utils import plot_history

if __name__ == "__main__":

    ga = Genetic(
        population_size=10,
        mutation_rate=1,
        generations=400,
        crossover_rate=1,
        problem=AckleyProblem(genes_boundaries=[(-5, 5), (-5, 5)]),
        crossover=ArithimeticCrossover(),
        selection=RouletteSelection(),
        mutation = UniformMutation(mutation_rate=1, mutation_value=0.15),
        verbose=1,
    )

    history, best_individual = ga.run()

    print("Best solution: ", best_individual.get_fitness())
    plot_history(history)