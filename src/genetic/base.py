from abc import ABC, abstractmethod
from .population import Population
from .individual import Individual
from .chromosome import Chromosome
from .gene import Gene


class Selection(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def select(
        self, population: Population, num_select: int, *args, **kwargs
    ) -> list[Individual]:
        raise NotImplementedError("Subclass must implement the mutate method.")
    


class Problem(ABC):

    @abstractmethod
    def __init__(
        self,
        mutation,
        genes_boundries: tuple = None,
        initial_state: Population = None,
    ):

        self.genes_boundries = genes_boundries
        self.initial_state = initial_state

        # Mutation operator
        if not isinstance(mutation, Mutation):
            raise TypeError(
                "Mutation operator must be an instance of Mutation or None"
            )
        else:
            self.mutation = mutation

        super().__init__()

    @abstractmethod
    def calculate_fitness(self, chromossome: Chromosome, *args, **kwargs):

        raise NotImplementedError("Subclass must implement the mutate method.")

    def generate_first_population(self, population_size):

        if self.initial_state is None:
            return self.generate_random_population(population_size)
        else:
            return self.initial_state

    def generate_random_population(self, population_size):
        population_list = []
        for i in range(population_size):
            # Create a chromosome with random genes
            chromosome = Chromosome(
                [
                    Gene(
                        low_boundry=boundary[0],
                        high_boundry=boundary[1]
                    )
                    for boundary in self.genes_boundries
                ]
            )
            # Create individual with chromosome
            individual = Individual(chromosome)
            # Add individual to population
            population_list.append(individual)
        return Population(population_list)
    

class Crossover(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def crossover(
        self, parent1: Individual, parent2: Individual, *args, **kwargs
    ) -> Individual:

        raise NotImplementedError("Subclass must implement the mutate method.")
    

class Mutation(ABC):

    @abstractmethod
    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate 

    @abstractmethod
    def mutate(
        self,
        value: any,
        high_boundry: any,
        low_boundry: any,
        *args,
        **kwargs
    ):
        
        raise NotImplementedError("Subclass must implement the mutate method.")