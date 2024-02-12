from abc import ABC, abstractmethod
from genetic.genetic.individual import Individual
from genetic.genetic.chromosome import Chromosome
from genetic.genetic.gene import Gene
from statistics import mean
import numpy as np


# ---------------------------------------------------------------------------------------------------
class Crossover(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def crossover(
        self, parent1: Individual, parent2: Individual, *args, **kwargs
    ) -> Individual:

        raise NotImplementedError("Subclass must implement the mutate method.")


# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------
class SinglePointCrossover(Crossover):

    def __init__(self):
        pass

    def crossover(
        self, parent1: Individual, parent2: Individual, *args, **kwargs
    ) -> Individual:

        random_point = np.random.randint(
            0, parent1.get_cromossom().get_cromossom_size()
        )
        child = Individual(
            Chromosome(
                parent1.get_cromossom().get_genes()[:random_point]
                + parent2.get_cromossom().get_genes()[random_point:]
            )
        )
        return child


# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------
class ArithimeticCrossover(Crossover):

    def __init__(self):
        pass

    def crossover(
        self, parent1: Individual, parent2: Individual, *args, **kwargs
    ) -> Individual:

        parent1_genes = parent1.get_cromossom().get_genes()
        parent2_genes = parent2.get_cromossom().get_genes()
        child_genes_values = [
            mean([parent1_genes[i].get_value(), parent2_genes[i].get_value()])
            for i in range(len(parent1_genes))
        ]
        child_genes = [
            Gene(
                low_boundry=parent1.get_cromossom().get_gene(i).get_boundries()[0],
                high_boundry=parent1.get_cromossom().get_gene(i).get_boundries()[1],
                value=child_genes_values[i],
                mutation=parent1.get_cromossom().get_gene(i).mutation,
            )
            for i in range(len(child_genes_values))
        ]
        return Individual(Chromosome(child_genes))


# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------
class UniformCrossover(Crossover):
    def __init__(self, genes_size):
        pass

    # TODO


# ---------------------------------------------------------------------------------------------------
