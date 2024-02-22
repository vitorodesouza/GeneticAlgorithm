from abc import ABC, abstractmethod
import numpy as np

from .individual import Individual
from .gene import Gene


class Mutation(ABC):

    @abstractmethod
    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate

    @abstractmethod
    def mutate(self, value: any, high_boundry: any, low_boundry: any, *args, **kwargs):

        raise NotImplementedError("Subclass must implement the mutate method.")


class UniformMutation(Mutation):

    def __init__(self, mutation_rate, mutation_value):
        super().__init__(mutation_rate)
        self.mutation_value = mutation_value

    def mutate(self, individual: Individual, *args, **kwargs):

        for gene in individual.get_chromosome().get_genes():
            gene.value = self.calculate_new_value(gene)

        return individual.get_chromosome()

    def calculate_new_value(self, gene: Gene):

        high_boundary = gene.high_boundry
        low_boundary = gene.low_boundry
        value = gene.value

        if np.random.uniform(0, 1) < self.mutation_rate:
            boundries_diff = high_boundary - low_boundary
            # mutation is done by adding a normally distributed random number to the gene's value
            new_value = min(
                max(
                    value
                    + np.random.uniform(
                        -boundries_diff * self.mutation_value,
                        boundries_diff * self.mutation_value,
                    ),
                    low_boundary,
                ),
                high_boundary,
            )
        return new_value
