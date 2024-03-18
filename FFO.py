import random
import math
import numpy as np

class FireFliesOptimizer:
    def __init__(self, fitness, x_min, x_max, beta_max=0.5, gamma=0.5, alpha=0.5, epochs=10, population_size=2, dimensions=1, patience=None):
        if beta_max >= 1 or beta_max <= 0 or gamma >= 1 or gamma <= 0 or alpha > 1 or alpha < 0:
            print("Incorrect parameters")
            return None
        self.fitness = fitness
        self.x_min = x_min
        self.x_max = x_max
        self.beta_max = beta_max
        self.epochs = epochs
        self.gamma = gamma
        self.alpha = alpha
        self.population_size =  population_size 
        self.dimensions = dimensions 
        self.patience = patience
        self._best = []
        self._meta = {"population": [], "fitness": [], "best_fitness": []}

    def fit(self):
        population_star = [(self.x_min[i]+(self.x_max[i]-self.x_min[i])*random.uniform(0, 1)) for i in range(self.dimensions)]
        population = []

        i = 0
        while i < self.population_size:
            x = [(self.x_min[i]+(self.x_max[i]-self.x_min[i])*random.uniform(0, 1)) for i in range(self.dimensions)]
            if x not in population:
                i += 1
                population.append(x)

        n = 0
        k = 0
        l = 0
        while n <= self.epochs and l < self.population_size:
            if self.fitness(*population[l]) <= self.fitness(*population[k]):
                beta = self.beta_max*math.exp(-self.gamma*(self.fitness(*population[l])-self.fitness(*population[k]))**2)
                for i in range(self.dimensions):
                    population[k][i] = population[k][i]+beta*(population[l][i]-population[k][i])+self.alpha*(random.uniform(0, 1)-0.5)
                    population[k][i] = max(self.x_min[i], population[k][i])
                    population[k][i] = min(self.x_max[i], population[k][i])
            if l < self.population_size - 1:
                l += 1
            elif k < self.population_size - 1:
                k += 1
                l = 0

            best = self.__get_fittest_individual__(population)
            if self.fitness(*population[best]) <= self.fitness(*population_star):
                population_star = population[best]
            self._meta["best_fitness"].append(self.fitness(*population_star))

            self._meta["population"].append(np.transpose(np.array(population)))
            fitness = []
            for args in population:
                result = self.fitness(*args)
                fitness.append(result)
            self._meta["fitness"].append(fitness)

            n += 1

        return population_star

            

    def __get_fittest_individual__(self, population):
        fitness = []
        
        # get fitness of population
        for args in population:
            result = self.fitness(*args)
            fitness.append(result)

        min_pos = fitness.index(min(fitness))
        return min_pos
    