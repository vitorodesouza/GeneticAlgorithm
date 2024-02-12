import numpy as np
from genetic.genetic.mutations import Mutation, UniformMutation


# ---------------------------------------------------------------------------------------------------
class Gene:

    def __init__(
        self,
        low_boundry: float,
        high_boundry: float,
        value: float = None,
        mutation: Mutation = None,
    ):

        self.low_boundry = low_boundry
        self.high_boundry = high_boundry

        # Mutation operator
        if mutation is None:
            self.mutation = UniformMutation(mutation_rate=1)  # Standard mutation method
        else:
            if not isinstance(mutation, Mutation):
                print("Mutation type: ", type(mutation))
                raise TypeError(
                    "Mutation operator must be an instance of Mutation or None"
                )
            else:
                self.mutation = mutation

        if value is not None:
            self.value = value
        else:
            self.value = self.generate_gene()

    def generate_gene(self):

        return np.random.uniform(self.low_boundry, self.high_boundry)

    def mutate(self) -> None:

        self.value = self.mutation.mutate(
            value=self.value,
            high_boundry=self.high_boundry,
            low_boundry=self.low_boundry
        )

    def get_value(self):

        return self.value

    def set_value(self, value):

        self.value = value

    def get_boundries(self):

        return (self.low_boundry, self.high_boundry)

    # str and repr for this gene
    def __str__(self):
        return f"Gene: {self.value}"

    def __repr__(self):
        return f"Gene: {self.value}"

    def __eq__(self, other):
        if not isinstance(other, Gene):
            return NotImplemented
        return self.value == other.value


# ---------------------------------------------------------------------------------------------------
