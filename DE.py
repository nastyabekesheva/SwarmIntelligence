import numpy as np
import matplotlib.pyplot as plt

class DifferentialEvolution:
    def __init__(self, objective_function, bounds, population_size=50, F=0.5, CR=0.9, epochs=1000):
        self.objective_function = objective_function
        self.bounds = bounds
        self.population_size = population_size
        self.F = F  
        self.CR = CR  
        self.epochs = epochs 
        self.best_fitnesses = []  
        
    def fit(self):
        n = len(self.bounds)
        
        population = np.random.uniform(low=self.bounds[:, 0], high=self.bounds[:, 1], size=(self.population_size, n))
        
        for i in range(self.epochs):
            #print("epoch ", i)
            new_population = np.zeros_like(population)
            for i in range(self.population_size):
                target = population[i]
                indices = [idx for idx in range(self.population_size) if idx != i]
                a, b, c = np.random.choice(indices, 3, replace=False)
                x1, x2, x3 = population[a], population[b], population[c]
                
                # Mutation
                mutant = x1 + self.F * (x2 - x3)
                mutant = np.clip(mutant, self.bounds[:, 0], self.bounds[:, 1])
                
                # Crossover
                mask = np.random.rand(n) < self.CR
                trial = np.where(mask, mutant, target)
                
                # Selection
                if self.objective_function(trial) < self.objective_function(target):
                    new_population[i] = trial
                else:
                    new_population[i] = target
                    
            population = new_population
            
            best_fitness = min(self.objective_function(individual) for individual in population)
            self.best_fitnesses.append(best_fitness)
            
                
        best_solution_idx = np.argmin([self.objective_function(individual) for individual in population])
        best_solution = population[best_solution_idx]
        best_fitness = self.objective_function(best_solution)
        return best_solution, best_fitness, self.best_fitnesses
    
    def plot_fitness(self):
        plt.figure()
        plt.plot(np.arange(len(self.best_fitnesses)), self.best_fitnesses, label='Best Fitness')
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.title('Evolution of Best Fitness')
        plt.legend()
        plt.grid(True)
        plt.show()