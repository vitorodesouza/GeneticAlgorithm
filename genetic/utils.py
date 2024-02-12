from matplotlib import pyplot as plt
from genetic.genetic.individual import Individual

def plot_history(history: list[Individual]) -> None:
    plt.plot([i.fitness for i in history])
    plt.ylabel("Fitness")
    plt.xlabel("Generation")
    plt.title("Fitness history")
    plt.show()
