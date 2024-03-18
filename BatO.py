import random
import numpy as np

class BatOptimizer:
    def __init__(self, fitness, x_min, x_max, f_min, f_max, freq=0.9, amplitude=1.9, alpha=0.5, gamma=0.5, delta=0.5, epochs=10, population_size=2, dimensions=1, patience=None):
        self.fitness = fitness
        self.x_min = x_min
        self.x_max = x_max
        self.f_min = f_min
        self.f_max = f_max
        self.freq = freq
        self.freq0 = freq
        self.amplitude = amplitude
        self.epochs = epochs
        self.alpha = alpha
        self.gamma = gamma
        self.delta = delta
        self.population_size =  population_size 
        self.dimensions = dimensions 
        self.patience = patience
        self._best = []
        self._meta = {"population": [], "fitness": [], "best_fitness": []}

    def fit(self):
        population = []
        velocity = []
        frequency = []

        j = 0
        while j < self.population_size:
            x = [self.x_min[i]+(self.x_max[i]-self.x_min[i])*random.uniform(0, 1) for i in range(self.dimensions)]
            if x not in population:
                j += 1
                population.append(x)
                velocity.append([0] * self.dimensions)
                frequency.append(self.f_min)

        population_star = population[self.__get_fittest_individual__(population)]
        
        n = 0
        while n < self.epochs:
            population, velocity, frequency = self.__modify__(population, velocity, frequency, population_star)
            self._meta["best_fitness"].append(self.fitness(*population_star))
            self._meta["population"].append(np.transpose(np.array(population)))
            fitness = []
            for args in population:
                result = self.fitness(*args)
                fitness.append(result)
            self._meta["fitness"].append(fitness)

            if random.uniform(0, 1) < self.freq * (n-1):
                population, population_star = self.__update_population__(n, population_star)

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
    
    def __modify__(self, population, velocity, frequency, population_star):
        for i in range(self.population_size):
            frequency[i] = self.f_min + (self.f_max - self.f_min) * random.uniform(0, 1)
            for k in range(self.dimensions):
                velocity[i][k] = velocity[i][k] + (population_star[k]-population[i][k]) * frequency[i]
                population[i][k] = max(self.x_min[k], population[i][k])
                population[i][k] = min(self.x_max[k], population[i][k])


        return population, velocity, frequency
    
    def __update_population__(self, n, population_star):
        x = []
        for i in range(self.population_size):
            xi = []
            for j in range(self.dimensions):
                xij = population_star[j] + self.delta * (self.x_max[j] - self.x_min[j]) * (-1 + 2 * random.uniform(0, 1))
                xij = max(self.x_min[j], xij)
                xij = min(self.x_max[j], xij)
                xi.append(xij)
            x.append(xi)

            if self.fitness(*xi) <= self.fitness(*population_star) and random.uniform(0, 1) < self.amplitude * (n - 1):
                population_star = xi
                self.amplitude = self.alpha * self.amplitude * (n-1) 
                self.freq = self.freq0 * (1 - np.exp(-self.gamma*n))

        return x, population_star
    

