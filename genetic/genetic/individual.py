from genetic.genetic.chromosome import Chromosome


class Individual:

    def __init__(self, chromossome: Chromosome):

        self.cromossom = chromossome
        self.fitness = None

    def set_cromossom(self, cromossom: Chromosome) -> None:

        self.cromossom = cromossom

    def get_cromossom(self) -> Chromosome:

        return self.cromossom

    def set_fitness(self, fitness) -> None:

        self.fitness = fitness

    def get_fitness(self) -> float:

        return self.fitness

    # str and repr for this individual
    def __str__(self):
        return f"Cromossom: {self.cromossom} | Fitness: {self.fitness}"

    def __repr__(self):
        return f"Cromossom: {self.cromossom} | Fitness: {self.fitness}"

    def __eq__(self, other):
        if not isinstance(other, Individual):
            return NotImplemented
        return self.cromossom == other.cromossom
