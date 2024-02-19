import numpy as np
from .chromosome import Chromosome
from .base import Problem



class AckleyProblem(Problem):

    def __init__(self, genes_boundries: tuple, mutation=None, initial_state=None):
        # self.genes_boundries = genes_boundries
        super().__init__(
            genes_boundries=genes_boundries,
            mutation=mutation,
            initial_state=initial_state,
        )

    def calculate_fitness(self, chromosome: Chromosome, *args, **kwargs):
        genes = chromosome.get_genes()
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

    def calculate_fitness(self, chromosome: Chromosome, *args, **kwargs):
        genes = chromosome.get_genes()
        return sum(1 for gene in genes if gene.value == 0)
