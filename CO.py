import random
import numpy as np

class CuckooOptimizer:
    def __init__(self, fitness, x_min, x_max, p_detect=0.8, delta=0.1, epochs=10, population_size=2, dimensions=1, patience=None):
        self.fitness = fitness
        self.x_min = x_min
        self.x_max = x_max
        self.p_detect = p_detect
        self.epochs = epochs
        self.delta = delta
        self.population_size =  population_size 
        self.dimensions = dimensions 
        self.patience = patience
        self._best = []
        self._meta = {"population": [], "fitness": [], "best_fitness": []}
    
    def fit(self):
        population = []

        j = 0
        while j < self.population_size:
            x = [self.x_min[i]+(self.x_max[i]-self.x_min[i])*random.uniform(0, 1) for i in range(self.dimensions)]
            if x not in population:
                j += 1
                population.append(x)

        population_star = population[self.__get_fittest_individual__(population)]


        n = 0
        while n < self.epochs:

            k = int(1 + (self.population_size - 1) * random.uniform(0, 1))
            population, population_star = self.__update_population__(population, k, population_star)
            self._meta["best_fitness"].append(self.fitness(*population_star))
            self._meta["population"].append(np.transpose(np.array(population)))
            fitness = []
            for args in population:
                result = self.fitness(*args)
                fitness.append(result)
            self._meta["fitness"].append(fitness)

            if random.uniform(0, 1) > self.p_detect:
                m = self.__get_least_fit_individual__(population)
                for j in range(self.dimensions):
                    xmj = population[m][j] + self.delta * (self.x_max[j] - self.x_min[j]) * (-1 + 2 * random.uniform(0, 1))
                    xmj = max(self.x_min[j], xmj)
                    xmj = min(self.x_max[j], xmj)
            
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
    
    def __get_least_fit_individual__(self, population):
        fitness = []
        
        # get fitness of population
        for args in population:
            result = self.fitness(*args)
            fitness.append(result)

        max_pos = fitness.index(max(fitness))
        return max_pos

    def __update_population__(self, population, k, population_star):
        x = []
        for i in range(self.population_size):
            xi = []
            for j in range(self.dimensions):
                xij = population[k][j] + self.delta * (self.x_max[j] - self.x_min[j]) * (-1 + 2 * random.uniform(0, 1))
                xij = max(self.x_min[j], xij)
                xij = min(self.x_max[j], xij)
                xi.append(xij)
            x.append(xi)

            if self.fitness(*xi) <= self.fitness(*population_star):
                population_star = xi

        return x, population_star
    
