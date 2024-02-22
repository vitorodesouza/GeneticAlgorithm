from genetic.problems import Problem
from .chromosome import Chromosome


class Individual:

    def __init__(self, chromossome: Chromosome):

        self.chromosome = chromossome
        self.fitness = None

    def set_chromosome(self, chromossome: Chromosome) -> None:

        self.chromosome = chromossome

    def get_chromosome(self) -> Chromosome:

        return self.chromosome

    
    def set_fitness(self, problema: Problem) -> None:

        if self.fitness is None:
            self.fitness = problema.calculate_fitness(self.chromosome)

    def get_fitness(self) -> float:

        return self.fitness

    # str and repr for this individual
    def __str__(self):
        return f"Chromosome: {self.chromosome} | Fitness: {self.fitness}"

    def __repr__(self):
        return f"Chromosome: {self.chromosome} | Fitness: {self.fitness}"

    def __eq__(self, other):
        if not isinstance(other, Individual):
            return NotImplemented
        return self.chromosome == other.chromosome
