from abc import ABC, abstractmethod
from statistics import mean
import numpy as np

from .individual import Individual
from .chromosome import Chromosome
from .gene import Gene


class Crossover(ABC):

    @abstractmethod
    def __init__(self, crossover_rate):
        self.crossover_rate = crossover_rate

    @abstractmethod
    def crossover(
        self, parent1: Individual, parent2: Individual, *args, **kwargs
    ) -> Individual:

        raise NotImplementedError("Subclass must implement the mutate method.")


class SinglePointCrossover(Crossover):

    def __init__(self, crossover_rate):
        super().__init__(crossover_rate)

    def crossover(
        self, parent1: Individual, parent2: Individual, *args, **kwargs
    ) -> Individual:

        if self.crossover_rate > np.random.uniform(0, 1):

            random_point = np.random.randint(
                0, parent1.get_chromosome().get_chromosome_size()
            )
            child = Individual(
                Chromosome(
                    parent1.get_chromosome().get_genes()[:random_point]
                    + parent2.get_chromosome().get_genes()[random_point:]
                )
            )

        return child


# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------
class ArithimeticCrossover(Crossover):

    def __init__(self, crossover_rate):
        super().__init__(crossover_rate)

    def crossover(
        self, parent1: Individual, parent2: Individual, *args, **kwargs
    ) -> Individual:

        if self.crossover_rate > np.random.uniform(0, 1):

            parent1_genes = parent1.get_chromosome().get_genes()
            parent2_genes = parent2.get_chromosome().get_genes()
            child_genes_values = [
                mean([parent1_genes[i].get_value(), parent2_genes[i].get_value()])
                for i in range(len(parent1_genes))
            ]
            child_genes = [
                Gene(
                    low_boundry=parent1.get_chromosome().get_gene(i).get_boundries()[0],
                    high_boundry=parent1.get_chromosome()
                    .get_gene(i)
                    .get_boundries()[1],
                    value=child_genes_values[i],
                )
                for i in range(len(child_genes_values))
            ]

        return Individual(Chromosome(child_genes))


# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------
class UniformCrossover(Crossover):
    def __init__(self, crossover_rate):
        super().__init__(crossover_rate)

    # TODO


# ---------------------------------------------------------------------------------------------------
