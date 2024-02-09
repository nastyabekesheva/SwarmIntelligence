import random

class GeneticOptimizer:
    def __init__(self, fitness, interval, iterations=10, population_size=2):
        self.fitness = fitness
        self.interval = interval
        self.iterations = iterations
        self.population_size =  int(2 * (population_size / 2 ))    

    def fit(self):
        i = 0
        population = random.sample(self. interval, self.population_size)
        while (i < self.iterations):
            new_population = self.__new_generation__(population)
            population = self.__get_fitest__(population, new_population)
            i += 1
            print(i)

        return (min(population), self.fitness(min(population)))
        
    def __new_generation__(self, parents):
        print("generating")
        bin_parents = ["{0:b}".format(i) for i in parents]
        bin_offsprings = []
        # normalize binary data
        max_bin_size = len(max(bin_parents))
        for i in range(len(bin_parents)):
            bin_parents[i] = "0" * (max_bin_size- len(bin_parents[i])) + bin_parents[i]
        # crossover
        for i in range(0, self.population_size, 2):
            breaking_point = random.randint(0, max_bin_size)
            bin_offsprings.append(bin_parents[i][0:breaking_point]+bin_parents[i+1][breaking_point:])
            bin_offsprings.append(bin_parents[i+1][0:breaking_point]+bin_parents[i][breaking_point:])
        # mutation by bit inversion
        for i in range(0, self.population_size):
            chance = random.uniform(0.0, 1.0)
            if chance < 0.3:
                bit_pos = random.randint(0, max_bin_size)
                if bin_offsprings[i] == "0":
                    bin_offsprings[i] = "1"
                else:
                    bin_offsprings[i] = "0"

        offsprings = [int(i, 2) for i in bin_offsprings]
        return offsprings
    
    def __get_fitest__(self, population, new_population):
        print("scoring")
        best_individuals = population
        best_fitness = [self.fitness(i) for i in population]

        for i in range(self.population_size):
            i_fitness = self.fitness(i)
            if i_fitness > min(best_fitness):
                min_pos = best_fitness.index(max(best_fitness))
                best_fitness.pop(min_pos)
                best_individuals.pop(min_pos)
                best_fitness.append(i_fitness)
                best_individuals.append(i)

        return best_individuals

            
    
        


import math 

def harmonic(x):
    return (x**3) * ((3-x)**5) * math.sin(10 * math.pi * x)

GO = GeneticOptimizer(harmonic, [0,3], iterations=10, population_size=2)
print(GO.fit())