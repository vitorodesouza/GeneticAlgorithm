from .mutations import Mutation
from .population import Population
from .crossovers import Crossover
from .problems import Problem
from .selections import Selection
from .population_generator import PopulationGenerator

from tqdm import tqdm


class Genetic:

    def __init__(
        self,
        population_size: int,
        generations: int,
        crossover,
        problem,
        selection,
        mutation,
        p_generator: PopulationGenerator = None,
        initial_state: Population = None,
        verbose: int = 0,
        **kwargs
    ):

        # Verbosity level
        self.verbose = verbose

        if self.verbose > 0:
            print("Initializing genetic algorithm")

        # Number of individuals in a population
        self.population_size = population_size
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

        if not isinstance(mutation, Mutation):
            raise TypeError("mutation must be an instance of Mutation")
        else:
            self.mutation = mutation

        # Initialize first generation
        if initial_state is not None:
            self.population = initial_state
        else:
            if p_generator is not None:
                # Use provided population generator
                if self.verbose > 0:
                    print("Generating first population")
                self.population = p_generator.generate(
                    population_size=self.population_size
                )
            else:
                # Use standard pop generator
                if self.verbose > 0:
                    print("Generating first population")
                self.population = PopulationGenerator(problem=self.problem).generate(
                    population_size=self.population_size
                )

        if verbose > 0:
            print("Genetic algorithm initialized")
        if verbose > 1:
            print("First population: ", self.population.individuals)

    def run(self):

        best_individuals_history = []
        for i in tqdm(range(self.generations), desc="Evolving Generations", ncols=100):

            # Calculate fitness values for each individual
            for individual in self.population.get_individuals():
                individual.set_fitness(self.problem)
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
        new_population = population

        for i in range(population_size):

            # Select two individuals from the sorted population
            parents = self.selection.select(population, num_select=2)
            # Creates a new individual by crossing the two selected individuals
            individual = self.crossover.crossover(parents[0], parents[1])
            # Mutates the new individual genes
            individual.chromosome = self.mutation.mutate(individual)

            # Calculate fitness for the new individual
            individual.set_fitness(self.problem)

            # Add the new individual to the new generation if new individual is
            # better than the worst individual in the previous generation
            if (
                individual.get_fitness()
                > population.get_worst_individual().get_fitness()
            ):
                new_population.individuals[0] = individual

        # Return a list with new individuals (next generation)
        return new_population

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
