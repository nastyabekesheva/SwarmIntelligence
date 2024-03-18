import random
import numpy as np

def norm(a, b):
    return np.sqrt(a ** 2 + b ** 2)

class GreyWolfOptimizer:

    """
    Optimizer for n-dimensional function
    """

    def __init__(self, fitness, interval, step=0.1, epochs=10, population_size=2, dimensions=1, patience=None):
        #population_size must be even
        if population_size % 2 != 0:
            print("Population size must be even")
            return None
        elif len(interval) != dimensions:
            print("Dimension of intervals do not match the dimension you provided")
            return None
        self.fitness = fitness
        self.interval = interval
        self.step = step
        self.epochs = epochs
        self.population_size =  int(2 * (population_size / 2 ))   
        self.dimensions = dimensions 
        self.patience = patience
        self._best = []
        self._meta = {"population": [], "fitness": []}

    def fit(self):

        # generate random population
        population = []
        for i in range(self.dimensions):
            population.append([random.uniform(*self.interval[i]) for _ in range(self.population_size)])
        
        fitness = []
        for args in zip(*population):
            result = self.fitness(*args)
            fitness.append(result)
        # save first population
        self._meta["population"].append(population)
        self._meta["fitness"].append(fitness)

        if self.patience:
            no_change = 0
        i = 0
        while (i < self.epochs):

            self._best.append(self.__get_fittest_individual__(i)[0])
            population = self.__chase__(population, self._best[i])
            fitness = self.__get_fitnes__(population)

            self._meta["population"].append(population)
            self._meta["fitness"].append(fitness)

            i += 1
            if self.patience:
                if self.__get_fittest_individual__(i) == self.__get_fittest_individual__(i-1):
                    no_change += 1
                else:
                    no_change = 0
                if no_change == self.patience:
                    break 

        return self.__get_fittest_individual__(i)
    
    def __chase__(self, population, best):
        new_population = []
        # the pack goes towards the pray 
        for i in range(self.dimensions):
            xi = []
            for j in range(len(population[i])):
                xi.append(population[i][j] + self.step * (best[i] - population[i][j]) / norm(best[i], population[i][j]))
            new_population.append(xi)

        return new_population

    def __get_fitnesS__(self, population):
        fitness = []
        for args in zip(*population):
            result = self.fitness(*args)
            fitness.append(result)
        return fitness

    def __get_fittest_individual__(self, i):

        min_pos = self._meta["fitness"][i].index(min(self._meta["fitness"][i]))
        return ([row[min_pos] for row in self._meta["population"][i]], self._meta["fitness"][i][min_pos])

