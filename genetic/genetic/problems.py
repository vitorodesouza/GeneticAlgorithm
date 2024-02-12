from abc import ABC, abstractmethod
import numpy as np
from genetic.genetic.chromosome import Chromosome
from genetic.genetic.gene import Gene
from genetic.genetic.individual import Individual
from genetic.genetic.mutations import Mutation, UniformMutation
from genetic.genetic.population import Population


class Problem(ABC):

    @abstractmethod
    def __init__(
        self,
        genes_boundries: tuple = None,
        mutation=None,
        initial_state: Population = None,
    ):

        self.genes_boundries = genes_boundries
        self.initial_state = initial_state

        # Mutation operator
        if mutation is None:
            self.mutation = UniformMutation(mutation_rate=1)  # Standard mutation method
        else:
            if not isinstance(mutation, Mutation):
                raise TypeError(
                    "Mutation operator must be an instance of Mutation or None"
                )
            else:
                self.mutation = mutation

        super().__init__()

    @abstractmethod
    def calculate_fitness(self, genes, *args, **kwargs):

        raise NotImplementedError("Subclass must implement the mutate method.")

    def generate_first_population(self, population_size):

        if self.initial_state is None:
            return self.generate_random_population(population_size)
        else:
            return self.initial_state

    def generate_random_population(self, population_size):
        population_list = []
        for i in range(population_size):
            # Create a cromossom with random genes
            cromossom = Chromosome(
                [
                    Gene(
                        low_boundry=boundary[0],
                        high_boundry=boundary[1],
                        mutation=self.mutation,
                    )
                    for boundary in self.genes_boundries
                ]
            )
            # Create individual with cromossom
            individual = Individual(cromossom)
            # Add individual to population
            population_list.append(individual)
        return Population(population_list)


class AckleyProblem(Problem):

    def __init__(self, genes_boundries: tuple, mutation=None, initial_state=None):
        # self.genes_boundries = genes_boundries
        super().__init__(
            genes_boundries=genes_boundries,
            mutation=mutation,
            initial_state=initial_state,
        )

    def calculate_fitness(self, genes, *args, **kwargs):
        gene_values = np.array([gene.get_value() for gene in genes])
        return -(
            -20 * np.exp(-0.2 * np.sqrt(np.mean(gene_values**2)))
            - np.exp(np.mean(np.cos(2 * np.pi * gene_values)))
            + 20
            + np.e
        )


class MaxZero(Problem):

    def __init__(self, genes_boundries: tuple, mutation=None, initial_state=None):
        # self.genes_boundries = genes_boundries
        super().__init__(
            genes_boundries=genes_boundries,
            mutation=mutation,
            initial_state=initial_state,
        )

    def calculate_fitness(self, genes, *args, **kwargs):
        return sum(1 for gene in genes if gene.value == 0)
