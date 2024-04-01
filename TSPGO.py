import numpy as np
import random

class TSPGeneticAlgorithm:
    def __init__(self, points, n_population=50, crossover_per=0.8, mutation_per=0.2, epochs=100):
        self.points = points
        self.n_population = n_population
        self.crossover_per = crossover_per
        self.mutation_per = mutation_per
        self.epochs = epochs
        self.paths_history = []

    def __initial_population__(self):
        population_perms = []
        possible_perms = list(range(len(self.points)))
        for _ in range(self.n_population):
            random.shuffle(possible_perms)
            population_perms.append(possible_perms[:])
        return population_perms

    def __distance__(self, point1, point2):
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    def __total_dist_individual__(self, individual):
        total_dist = 0
        for i in range(len(individual)):
            total_dist += self.__distance__(self.points[individual[i]], self.points[individual[(i + 1) % len(individual)]])
        return total_dist

    def __fitness_prob__(self, population):
        total_dist_all_individuals = [self.__total_dist_individual__(individual) for individual in population]
        max_population_cost = max(total_dist_all_individuals)
        population_fitness = [max_population_cost - dist for dist in total_dist_all_individuals]
        population_fitness_sum = sum(population_fitness)
        population_fitness_probs = [fitness / population_fitness_sum for fitness in population_fitness]
        return population_fitness_probs

    def __roulette_wheel__(self, population, fitness_probs):
        population_fitness_probs_cumsum = np.cumsum(fitness_probs)
        selected_individual_index = np.argmax(population_fitness_probs_cumsum > random.uniform(0, 1))
        return population[selected_individual_index][:]

    def __crossover__(self, parent_1, parent_2):
        n_cities_cut = len(parent_1) - 1
        cut = round(random.uniform(1, n_cities_cut))
        offspring_1 = parent_1[0:cut] + [city for city in parent_2 if city not in parent_1[0:cut]]
        offspring_2 = parent_2[0:cut] + [city for city in parent_1 if city not in parent_2[0:cut]]
        return offspring_1, offspring_2

    def __mutation__(self, offspring):
        n_cities_cut = len(offspring) - 1
        index_1 = round(random.uniform(0, n_cities_cut))
        index_2 = round(random.uniform(0, n_cities_cut))
        temp = offspring[index_1]
        offspring[index_1] = offspring[index_2]
        offspring[index_2] = temp
        return offspring

    def fit(self):
        population = self.__initial_population__()
        for _ in range(self.epochs):
            fitness_probs = self.__fitness_prob__(population)
            parents_list = [self.__roulette_wheel__(population, fitness_probs) for _ in range(int(self.crossover_per * self.n_population))]
            offspring_list = []
            for i in range(0, len(parents_list), 2):
                offspring_1, offspring_2 = self.__crossover__(parents_list[i], parents_list[i+1])
                if random.random() > (1 - self.mutation_per):
                    offspring_1 = self.__mutation__(offspring_1)
                if random.random() > (1 - self.mutation_per):
                    offspring_2 = self.__mutation__(offspring_2)
                offspring_list.append(offspring_1)
                offspring_list.append(offspring_2)
            mixed_offspring = parents_list + offspring_list
            fitness_probs = self.__fitness_prob__(mixed_offspring)
            sorted_fitness_indices = np.argsort(fitness_probs)[::-1]
            best_fitness_indices = sorted_fitness_indices[0:int(0.8 * self.n_population)]
            best_mixed_offspring = [mixed_offspring[i] for i in best_fitness_indices]
            old_population_indices = [random.randint(0, (self.n_population - 1)) for _ in range(int(0.2 * self.n_population))]
            for i in old_population_indices:
                best_mixed_offspring.append(population[i])
            random.shuffle(best_mixed_offspring)
            population = best_mixed_offspring
            self.paths_history.append(best_mixed_offspring)
        return population
