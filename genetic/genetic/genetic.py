from genetic.genetic.population import Population
from genetic.genetic.crossovers import Crossover
from genetic.genetic.problems import Problem
from genetic.genetic.selections import Selection
from genetic.genetic.chromosome import Chromosome
from genetic.genetic.gene import Gene
from genetic.genetic.individual import Individual


class Genetic:

    def __init__(
        self,
        population_size: int,
        crossover_rate: float,
        generations: int,
        crossover,
        problem,
        selection,
        verbose: int = 0,
        **kwargs
    ):

        # Verbosity level
        self.verbose = verbose

        if self.verbose > 0:
            print("Initializing genetic algorithm")

        # Number of individuals in a population
        self.population_size = population_size
        # Probability of crossover between two individuals
        self.crossover_rate = crossover_rate
        # Number of generations to run the algorithm
        self.generations = generations

        # Crossover operator
        if not isinstance(crossover, Crossover):
            raise TypeError("crossover must be an instance of Crossover")
        else:
            self.crossover = crossover

        # Problem
        if not isinstance(problem, Problem):
            raise TypeError("problem must be an instance of Problem")
        else:
            self.problem = problem

        # Selection operator
        if not isinstance(selection, Selection):
            raise TypeError("selection must be an instance of Selection")
        else:
            self.selection = selection

        # Initialize first generation
        if self.verbose > 0:
            print("Generating first population")
        self.population = self.problem.generate_first_population(
            population_size=self.population_size
        )

        if verbose > 0:
            print("Genetic algorithm initialized")
        if verbose > 0:
            print("First population: ", self.population.individuals)

    def run(self):

        best_individuals_history = []
        for i in range(self.generations):

            if self.verbose > 0:
                print("Generation: ", i)

            # Calculate fitness values for each individual
            for individual in self.population.get_individuals():
                individual.set_fitness(
                    self.problem.calculate_fitness(
                        individual.get_cromossom().get_genes()
                    )
                )
            # Get best individual from new generation
            best_individuals_history.append(self.population.get_best_individual())
            # Create next generation
            new_population = self.create_next_generation(self.population)
            # Set new population as current population
            self.population = new_population
        # Return the history of best individuals and the best individual of currrent population
        return best_individuals_history, self.population.get_best_individual()

    def create_next_generation(self, population: Population):

        # Get population lenght
        population_size = len(population.get_individuals())
        # Get list of individuals sorted by fitness in ascending order
        population.sort_individuals_by_fitness()

        for i in range(population_size):

            # Select two individuals from the sorted population
            parents = self.selection.select(population, num_select=2)
            # Creates a new individual by crossing the two selected individuals
            individual = self.crossover.crossover(parents[0], parents[1])
            # Mutates the new individual genes
            for gene in individual.get_cromossom().get_genes():
                gene.mutate()

            # Calculate fitness for the new individual
            individual.set_fitness(
                self.problem.calculate_fitness(individual.get_cromossom().get_genes())
            )
            # Add the new individual to the new generation if new individual is
            # better than the worst individual in the previous generation
            if (
                individual.get_fitness()
                > population.get_worst_individual().get_fitness()
            ):
                population.set_individual(0, individual)

        # Return a list with new individuals (next generation)
        return population

    def sort_population_by_fitness(self, population: Population):
        return sorted(
            population.get_individuals(),
            key=lambda individual: individual.get_fitness(),
        )


if __name__ == "__main__":
    print("Genetic algorithm implementation")
    print("by: Vitor Oliveira de Souza - vitor.odesouza@gmail.com")


# TODO: Check these:
# hypervolume
# jmetal - jmetalpy
