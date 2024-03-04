import random
import math

class ParticleSwarmOptimizer:
    def __init__(self, fitness, x_min, x_max, v_min, v_max, alpha1=0.5, alpha2=0.5, epochs=10, population_size=2, dimensions=1, patience=None):
        if alpha1 >= 4 or alpha1 <= 0 or alpha2 >= 4 or alpha2 <= 0:
            print("Incorrect parameters")
            return None
        self.fitness = fitness
        self.x_min = x_min
        self.x_max = x_max
        self.v_min = v_min
        self.v_max = v_max
        self.alpha1 = alpha1
        self.epochs = epochs
        self.alpha2 = alpha2
        self.population_size =  population_size 
        self.dimensions = dimensions 
        self.patience = patience
        self._best = []
        self._meta = {"population": [], "fitness": []}

    def fit(self):
        population = []
        velocity = []

        i = 0
        while i < self.population_size:
            x = [(self.x_min[i]+(self.x_max[i]-self.x_min[i])*random.uniform(0, 1)) for i in range(self.dimensions)]
            v = [(self.v_min[i]+(self.v_max[i]-self.v_min[i])*random.uniform(0, 1)) for i in range(self.dimensions)]
            if x not in population and v not in velocity:
                i += 1
                population.append(x)
                velocity.append(v)

        population_star = population[self.__get_fittest_individual__(population)]
        population_best = population
        n = 0
        k = 1
        while n < self.epochs:
            velocity = self.__update_velocity__(velocity, population_best, population, population_star)
            population, velocity = self.__update_population__(population, velocity)

            for i in range(self.population_size):
                if self.fitness(*population[i]) <= self.fitness(*population_best[i]):
                    population_best[i] = population[i]
            
            star = population[self.__get_fittest_individual__(population)]
            if self.fitness(*star) <= self.fitness(*population_star):
                population_star = star
            n += 1

        return(population_star)
        
    def __get_fittest_individual__(self, population):
        fitness = []
        
        # get fitness of population
        for args in population:
            result = self.fitness(*args)
            fitness.append(result)

        min_pos = fitness.index(min(fitness))
        return min_pos
            
    def __update_velocity__(self, velocity, population_best, population, population_star):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        v = []
        for i in range(self.population_size):
            vi = []
            for j in range(self.dimensions):
                vij = velocity[i][j] + self.alpha1*(population_best[i][j]  - population[i][j] )*r1 + self.alpha2*(population_star[j] - population[i][j] )*r2
                vij = max(self.x_min[j], vij)
                vij = min(self.x_max[j], vij)
                vi.append(vij)
            v.append(vi)

        return v

    def __update_population__(self, population, velocity):
        x = []
        for i in range(self.population_size):
            xi = []
            for j in range(self.dimensions):
                xij = population[i][j] + velocity[i][j] 
                if xij < self.x_min[j]:
                    xij = self.x_min[j] + abs(xij - self.x_min[j])
                    velocity[i][j] = -velocity[i][j]
                elif xij > self.x_max[j]:
                    xij = self.x_max[j] + abs(xij - self.x_max[j])
                    velocity[i][j] = -velocity[i][j]
                xi.append(xij)
            x.append(xi)
        return x, velocity
        
def rosenbrock(x, y):
    f = (1-x)**2+100*(y-x**2)**2
    if (x-1)**3-y+1<0 or x+y-2<0:
        f = float('inf')

    return f

PSO = ParticleSwarmOptimizer(rosenbrock, [-1.5, -0.5], [1.5, 2.5], [1, 1], [5, 5], epochs=50, population_size=10, dimensions=2)
print(PSO.fit())