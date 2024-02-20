


import random
from .chromosome import Chromosome
from .individual import Individual
from .population import Population
from .gene import Gene
from .problems_types import ProblemDataType, ProblemType
from .problems import Problem


class PopulationGenerator:
      
    def __init__(self, problem:Problem):
        self.p_type = problem.problem_type
        self.p_dtype = problem.problem_data_type
        self.problem = problem

    def generate(self,population_size: int):
        match self.p_dtype:
            case ProblemDataType.REAL:
                if self.problem.genes_boundaries is None:
                    raise ValueError("genes_boundaries must be provided")
                return self.continuous_population(population_size=population_size, genes_boundaries=self.problem.genes_boundaries)
            case ProblemDataType.CATEGORICAL:
                if self.problem.categories is None:
                    raise ValueError("categories must be provided")
                return self.discrete_population(population_size=population_size, categories=self.problem.categories)
            case _:
                raise ValueError("Invalid problem type or not implemented yet")


    def continuous_population(self, population_size: int, genes_boundaries: list):
        population_list = []
        for i in range(population_size):
            # Create a chromosome with random genes
            chromosome = Chromosome(
                [
                    Gene(
                        value = random.uniform(boundary[0], boundary[1]),
                        low_boundry=boundary[0],
                        high_boundry=boundary[1]
                    )
                    for boundary in genes_boundaries
                ]
            )
            # Create individual with chromosome
            individual = Individual(chromosome)
            # Add individual to population
            population_list.append(individual)
        return Population(population_list)


    def discrete_population(self, population_size: int, categories: list):
        population_list = []
        for i in range(population_size):
            # Generate random sequence of cities
            random_sequence = random.sample(categories, len(categories))
            # Create a cromossom with random genes
            cromossom = Chromosome(
                [
                    Gene(
                        low_boundry=None,
                        high_boundry=None,
                        value = categories[sequence]
                    )
                    for sequence in random_sequence
                ]
            )
            # Create individual with cromossom
            individual = Individual(cromossom)
            # Add individual to population
            population_list.append(individual)
        return Population(population_list)
