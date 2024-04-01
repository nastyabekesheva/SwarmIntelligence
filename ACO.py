import numpy as np
import matplotlib.pyplot as plt

class AntColonyOptimization:
    def __init__(self, points, n_ants, epochs, alpha, beta, evaporation_rate, Q):
        self.points = points
        self.Q = Q
        self.evaporation_rate = evaporation_rate
        self.beta = beta
        self.alpha = alpha
        self.epochs = epochs
        self.n_ants = n_ants
        self._meta = []
        

    def __distance__(self, point1, point2):
        return np.sqrt(np.sum((point1 - point2)**2))

    def fit(self):
        n_points = len(self.points)
        pheromone = np.ones((n_points, n_points))
        best_path = None
        best_path_length = np.inf
        
        for _ in range(self.epochs):
            paths = []
            path_lengths = []
            
            for ant in range(self.n_ants):
                visited = [False]*n_points
                current_point = np.random.randint(n_points)
                visited[current_point] = True
                path = [current_point]
                path_length = 0
                
                while False in visited:
                    unvisited = np.where(np.logical_not(visited))[0]
                    probabilities = np.zeros(len(unvisited))
                    
                    for i, unvisited_point in enumerate(unvisited):
                        probabilities[i] = pheromone[current_point, unvisited_point]**self.alpha / self.__distance__(self.points[current_point], self.points[unvisited_point])**self.beta
                    
                    probabilities /= np.sum(probabilities)
                    
                    next_point = np.random.choice(unvisited, p=probabilities)
                    path.append(next_point)
                    path_length += self.__distance__(self.points[current_point], self.points[next_point])
                    visited[next_point] = True
                    current_point = next_point
                
                paths.append(path)
                path_lengths.append(path_length)
                
                if path_length < best_path_length:
                    best_path = path
                    best_path_length = path_length
            
            pheromone *= self.evaporation_rate
            
            for path, path_length in zip(paths, path_lengths):
                for i in range(n_points-1):
                    pheromone[path[i], path[i+1]] += self.Q/path_length
                pheromone[path[-1], path[0]] += self.Q/path_length

            self._meta.append(best_path)
        
        return best_path, self.points[best_path]



