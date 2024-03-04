import random
import numpy as np

class BeeOptimizer:
    def __init__(self, fitness, num_areas, num_elite_areas, elite_area_size, area_size, x_min, x_max, delta=0.5, eta_max=0.5, alpha=0.5, epochs=10, population_size=2, dimensions=1, patience=None):
        if delta >= 1 or delta <= 0 or eta_max >= 1 or eta_max <= 0 or alpha >= 1 or alpha <= 0:
            print("Incorrect parameters")
            return None
        self.fitness = fitness
        self.num_areas = num_areas
        self.num_elite_areas = num_elite_areas
        self.elite_area_size = elite_area_size
        self.area_size = area_size
        self.x_min = x_min
        self.x_max = x_max
        self.delta = delta
        self.epochs = epochs
        self.eta_max = eta_max
        self.alpha = alpha
        self.population_size =  population_size 
        self.dimensions = dimensions 
        self.patience = patience
        self._best = []
        self._meta = {"population": [], "fitness": []}

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
        while n <= self.epochs:
            best = population[self.__get_fittest_individual__(population)]
            if self.fitness(*best) <= self.fitness(*population_star):
                population_star = best

            self._meta["best_fitness"].append(self.fitness(*population_star))

            population = self.__sort__(population)
            population = self.__bee_workers__(n , population) + self.__bee_scouts__()
            n += 1

            self._meta["population"].append(np.transpose(np.array(population)))
            fitness = []
            for args in population:
                result = self.fitness(*args)
                fitness.append(result)
            self._meta["fitness"].append(fitness)

        return population_star


    def __get_fittest_individual__(self, population):
        fitness = []
        
        # get fitness of population
        for args in population:
            result = self.fitness(*args)
            fitness.append(result)

        min_pos = fitness.index(min(fitness))
        return min_pos
    
    def __sort__(self, population):
        if len(population) <= 1:
            return population
        
        pivot = population[len(population) // 2]  # Choose a pivot element
        left = [individual for individual in population if self.fitness(*individual) > self.fitness(*pivot)]
        middle = [individual for individual in population if self.fitness(*individual) == self.fitness(*pivot)]
        right = [individual for individual in population if self.fitness(*individual) < self.fitness(*pivot)]
        
        return self.__sort__(left) + middle + self.__sort__(right)
    
    def __bee_workers__(self, n, population):
        neighbourhood = []
        l = 0
        if l <= self.num_elite_areas:
            Z = self.elite_area_size
        else:
            Z = self.area_size

        while l <= self.num_areas:
            x_hat = []
            eta = self.eta_max*self.alpha**n

            for z in range(Z):
                x_z = []
                for i in range(self.dimensions):
                    x_zi = population[l][z] + eta*self.delta*(self.x_max[i] - self.x_min[i])*(1-2*random.uniform(0, 1))
                    x_zi = max(self.x_min[i], x_zi)
                    x_zi = min(self.x_max[i], x_zi)
                    x_z.append(x_zi)
                x_hat.append(x_z)

            neighbourhood.append(x_hat[self.__get_fittest_individual__(x_hat)])
            l += 1

        return neighbourhood
    
    def __bee_scouts__(self):
        return [[(self.x_min[i]+(self.x_max[i]-self.x_min[i])*random.uniform(0, 1)) for i in range(self.dimensions)] for _ in range(self.num_areas, self.population_size)]
