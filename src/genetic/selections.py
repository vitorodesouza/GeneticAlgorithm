from abc import ABC, abstractmethod
from .population import Population
from .individual import Individual
from .base import Selection
import numpy as np



class TournamentSelection(Selection):
    def __init__(self, tournament_size):
        pass

    # TODO

class RankSelection(Selection):
    def __init__(self):
        pass

    # TODO

class RandomSelection(Selection):
    def __init__(self):
        pass

    def select(
        self, population: Population, num_select: int, *args, **kwargs
    ) -> list[Individual]:
        if not isinstance(num_select, int) or num_select < 1:
            raise ValueError("num_select must be a positive integer")
        selected_individuals = []
        for i in range(num_select):
            selected_individuals.append(
                population.get_individuals()[
                    np.random.randint(0, len(population.get_individuals()))
                ]
            )
        return selected_individuals

class RouletteSelection(Selection):

    def __init__(self):
        pass

    def select(
        self, population: Population, num_select: int, *args, **kwargs
    ) -> list[Individual]:
        selected_individuals = []
        for i in range(num_select):
            offset = 0
            normalized_fitness_sum = sum(
                [
                    individual.get_fitness()
                    for individual in population.get_individuals()
                ]
            )
            lowest_fitness = population.get_worst_individual().get_fitness()
            if lowest_fitness < 0:
                offset = -lowest_fitness
                normalized_fitness_sum += offset * len(population.get_individuals())

            draw = np.random.uniform(0, 1)
            accumulated = 0

            for individual in population.get_individuals():
                fitness = individual.get_fitness() + offset
                probability = fitness / normalized_fitness_sum
                accumulated += probability

                if draw <= accumulated:
                    selected_individuals.append(individual)
                    break

        if len(selected_individuals) < num_select:
            print(
                "RouletteSelection could not select all parents based on current population, this is probably because all Individuals are equal to each other"
            )
            print("selected_individuals: ", len(selected_individuals))
            print("num_select: ", num_select)
            print("Next individuals will be selected randomly")
            for j in range(num_select - len(selected_individuals)):
                selected_individuals.append(
                    population.get_individuals()[
                        np.random.randint(0, len(population.get_individuals()))
                    ]
                )

        return selected_individuals#[selected_individuals[i] for i in range(num_select)]

