# Import to ignore typing annotations
from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np

# from .population import Population
from .chromosome import Chromosome
from .problems_types import ProblemDataType, ProblemType


class Problem(ABC):

    problem_type: ProblemType = None  # Needs to be defined for each problem
    problem_data_type: ProblemDataType = None  # Needs to be defined for each problem
    problem_description: str = None  # Needs to be defined for each problem

    @abstractmethod
    def __init__(
        self,
        genes_boundaries: tuple = None,
        initial_state: Population = None,
    ):

        self.genes_boundaries = genes_boundaries
        self.initial_state = initial_state
        super().__init__()

    @abstractmethod
    def calculate_fitness(self, chromossome: Chromosome, *args, **kwargs):

        raise NotImplementedError("Subclass must implement the mutate method.")


class AckleyProblem(Problem):

    problem_type: ProblemType = ProblemType.MAXIMIZE
    problem_data_type: ProblemDataType = ProblemDataType.REAL
    problem_description: str = "Maximize the value for Ackley's function"

    def __init__(self, genes_boundaries: tuple, initial_state=None):
        # self.genes_boundaries = genes_boundaries
        super().__init__(
            genes_boundaries=genes_boundaries,
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

    problem_type: ProblemType = ProblemType.MAXIMIZE
    problem_data_type: ProblemDataType = ProblemDataType.BINARY
    problem_description: str = "Maximize the number of zeros"

    def __init__(self, genes_boundaries: tuple, initial_state=None):
        # self.genes_boundaries = genes_boundaries
        super().__init__(genes_boundaries=genes_boundaries, initial_state=initial_state)

        self.problem_type = "max"
        self.problem_data_type = "discrete"

    def calculate_fitness(self, chromosome: Chromosome, *args, **kwargs):
        genes = chromosome.get_genes()
        return sum(1 for gene in genes if gene.value == 0)
