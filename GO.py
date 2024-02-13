import random
#from itertools import product
import numpy as np
import re

def pop_column(matrix, pos):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(matrix[i][:pos] + matrix[i][pos+1:])
    return new_matrix

def insert_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i].append(column[i])
    return matrix

def bin_to_float(bin, interval):
    return (int(bin, 2) / (2 ** 16 - 1)) * (interval[1] - interval[0]) + interval[0]

def float_to_bin(value, interval):
    binary_str = bin(int((value - interval[0]) / (interval[1] - interval[0]) * (2 ** 16 - 1)))
    new = re.sub(r'^(-?)0b', r'\1', binary_str) 
    return new

class GeneticOptimizer:
    #population_size must be even
    def __init__(self, fitness, interval, epochs=10, population_size=2, dimensions=1):
        if population_size % 2 != 0:
            print("Population size must be even")
            return None
        elif len(interval) != dimensions:
            print("Dimension of intervals do not math the dimension you provided")
            return None
        self.fitness = fitness
        self.interval = interval
        self.epochs = epochs
        self.population_size =  int(2 * (population_size / 2 ))   
        self.dimensions = dimensions 
        self._meta = {"population": [], "fitness": []}

    def fit(self):
        i = 0
        # generate random population
        population = []
        for i in range(self.dimensions):
            population.append([random.uniform(*self.interval[i]) for _ in range(self.population_size)])
        while (i < self.epochs):
            new_population = self.__new_generation__(population)
            population = self.__get_fitest__(population, new_population)
            i += 1

        return self.__get_fittest_individual__(population)
        
    def __new_generation__(self, parents):
        offsprings = []
        for j in range(self.dimensions):
            bin_parents = [float_to_bin(i, self.interval[j]) for i in parents[j]]
            #bin_parents = ["{0:b}".format(i) for i in parents[j]]
            bin_offsprings = []
            # normalize binary data
            max_bin_size = max(len(bin_parent) for bin_parent in bin_parents)
            bin_parents = [bin_parent.zfill(max_bin_size) for bin_parent in bin_parents]
            # crossover
            for i in range(0, self.population_size, 2):
                breaking_point = random.randint(0, max_bin_size-1)
                bin_offsprings.append(bin_parents[i][0:breaking_point]+bin_parents[i+1][breaking_point:])
                bin_offsprings.append(bin_parents[i+1][0:breaking_point]+bin_parents[i][breaking_point:])
            # mutation by bit inversion
            for i in range(0, self.population_size):
                if random.random() < 0.3:
                    pos = random.randint(0, max_bin_size-1)
                    if bin_offsprings[i][pos] == "0":
                        bin_offsprings[i] = bin_offsprings[i][:pos] + "1"  + bin_offsprings[i][pos+1:]
                    else:
                        bin_offsprings[i] = bin_offsprings[i][:pos] + "0"  + bin_offsprings[i][pos+1:]

            offsprings.append([bin_to_float(i, self.interval[j]) for i in bin_offsprings])
        return offsprings
    
    def __get_fitest__(self, population, new_population):
        #print(population)
        best_individuals = population
        best_fitness = []
        
        # get fitness of old population
        for args in zip(*population):
            result = self.fitness(*args)
            best_fitness.append(result)

        # select only best individuals
        for args in zip(*new_population):
            i_fitness = self.fitness(*args)
            if i_fitness < min(best_fitness):
                max_pos = best_fitness.index(max(best_fitness))
                best_fitness.pop(max_pos)
                best_individuals = pop_column(best_individuals, max_pos)
                best_fitness.append(i_fitness)
                best_individuals = insert_column(best_individuals, args)

        self._meta["population"].append(best_individuals)
        self._meta["fitness"].append(best_fitness)
        return best_individuals

                
    def __get_fittest_individual__(self, population):
        fitness = []
        
        # get fitness of population
        for args in zip(*population):
            result = self.fitness(*args)
            fitness.append(result)

        min_pos = fitness.index(min(fitness))
        return [row[min_pos] for row in population], fitness[min_pos]


        '''fitness = {}
        # combine two generations
        potential_population = [population[i] + new_population[i] for i in range(self.dimensions)]

        # create possible combinations
        combinations_list = []
        other_rows_indices = [i for i in range(self.dimensions) if i != 0]
        for element in potential_population[0]:
            for other_row_indices in product(*[[potential_population[j][k] for k in range(self.population_size)] for j in other_rows_indices]):
                flat_combination = (element,) + tuple(other_row_indices)
                combinations_list.append(flat_combination)
        # get fitness of combinations
        for combination in combinations_list:
            fitness.update({combination: self.fitness(combination)})
        # get fittest combinations
        inverted_dict = [(value, key) for key, value in fitness.items()]
        smallest_items = heapq.nsmallest(self.population_size, inverted_dict)
        smallest_keys = [item[1] for item in smallest_items]'''
                   
            
import math 

def harmonic(x):
    return (x**3) * ((3-x)**5) * math.sin(10 * math.pi * x)

def izum(x, y):
    return - math.cos(x) * math.cos(y) * math.exp(-(x-math.pi) ** 2 -(y-math.pi) ** 2)

def erkli(x, y):
    return (-20 * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.exp(1) + 20)

GO = GeneticOptimizer(izum, [[-100, 100], [-100, 100]], epochs=15, population_size=50, dimensions=2)
#GO = GeneticOptimizer(harmonic, [[0, 3]], epochs=30, population_size=10, dimensions=1)
print(GO.fit())
print(GO._meta)
