import random

class ParticleSwarmOptimizer:
    def __init__(self, fitness, interval, epochs=10, population_size=10, dimensions=1, patience=None, a1=1, a2=2):
        #population_size must be even
        if population_size % 2 != 0:
            print("Population size must be even")
            return None
        elif len(interval) != dimensions:
            print("Dimension of intervals do not match the dimension you provided")
            return None
        self.fitness = fitness
        self.interval = interval
        self.epochs = epochs
        self.population_size = population_size
        self.dimensions = dimensions 
        self.patience = patience
        self.a1 = a1
        self.a2 = a2
        self._meta = {"population": [], "fitness": []}

    def fit(self):
        population = []
        population_velocity = []
        best = []

        for i in range(self.population_size):
            x, v = self.__init_population__()
            population.append(x)

        population_record, fitness, k = self.__get_fittest_individual__(population)

        i = 0
        while i <= self.epochs:
            for k in range(self.dimensions):
                population_velocity.append(self.__modify_velocity__(population_velocity[k]), best[k])
                population.append(population[k], best[k])
             

    def __init_population__(self):
        x_min = []
        x_max = []
        self.v_min = []
        self.v_max = []

        for i in range(self.dimensions):
            x_min.append(random.uniform(self.interval[i][0], (self.interval[i][1] - 1) / 2))
            x_max.append(random.uniform(x_min, self.interval[i][1] / 2))
            tmp = len(str(self.interval[i][1] - self.interval[i][0]))
            self.v_min.append(random.uniform((1 / 100) * tmp, (1 / 10) * tmp))
            self.v_max.append(random.uniform(self.v_min, (1 / 10) * tmp))

        x = []
        v = []

        for i in range(self.dimensions):
            x.append(x_min[i] + (x_max[i]-x_min[i]) * random.uniform(0, 1))
            v.append(self.v_min[i] + (self.v_max[i]-self.v_min[i]) * random.uniform(0, 1))

        return x, v
    
    def __get_fittest_individual__(self, population):
        fitness = []
        
        # get fitness of population
        for args in zip(*population):
            result = self.fitness(*args)
            fitness.append(result)

        min_pos = fitness.index(min(fitness))
        return [row[min_pos] for row in population], fitness[min_pos], min_pos
    
    def __modify_velocity__(self, velocity, best):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)

        v = []

        for k in range(self.population_size):
            v.append(velocity[k] + self.a1())

        return v
    
    def __modify_position__(self, population, best):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)

        v = []

        for k in range(self.population_size):
            v.append(population[k] + self.a1())

        return v