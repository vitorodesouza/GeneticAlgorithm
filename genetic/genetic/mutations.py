from abc import ABC, abstractmethod
import numpy as np


# TODO: Implementing mutation as an class for each gene


# ---------------------------------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------
class UniformMutation(Mutation):

    def __init__(self, mutation_rate):
        super().__init__(mutation_rate)

    def mutate(
        self,
        value: float,
        high_boundry: any,
        low_boundry: any,
        *args,
        **kwargs
    ):

        if np.random.uniform(0, 1) < self.mutation_rate:
            boundries_diff = high_boundry - low_boundry
            # mutation is done by adding a normally distributed random number to the gene's value
            new_value = min(
                max(
                    value + np.random.normal(-boundries_diff / 50, boundries_diff / 50),
                    low_boundry,
                ),
                high_boundry,
            )
        return new_value


# ---------------------------------------------------------------------------------------------------
