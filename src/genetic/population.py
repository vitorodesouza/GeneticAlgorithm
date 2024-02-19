from .individual import Individual


class Population:

    def __init__(self, individuals: list[Individual]):

        self.set_individuals(individuals)

    def set_individuals(self, individuals: list[Individual]) -> None:

        self.individuals = individuals

    def get_individuals(self) -> list[Individual]:

        return self.individuals

    def get_num_individuals(self) -> int:

        return len(self.individuals)

    def get_individual(self, index: int) -> Individual:

        return self.individuals[index]

    def set_individual(self, index: int, individual: Individual) -> None:

        self.individuals[index] = individual

    def add_individual(self, individual: Individual) -> None:

        self.individuals.append(individual)

    def remove_individual(self, index: int) -> None:

        self.individuals.pop(index)

    def get_best_individual(self) -> Individual:

        return max(self.individuals, key=lambda x: x.get_fitness())

    def get_worst_individual(self) -> Individual:

        return min(self.individuals, key=lambda x: x.get_fitness())

    def sort_individuals_by_fitness(self) -> None:

        self.individuals.sort(key=lambda x: x.get_fitness())

    # str and repr for this population
    def __str__(self):
        return f"Population: {self.individuals}"

    def __repr__(self):
        return f"Population: {self.individuals}"
