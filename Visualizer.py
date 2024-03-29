import matplotlib.pyplot as plt
import numpy as np
import imageio

class Visualizer:
    def __init__(self, data, func, interval, fps=10, filename="f", dimensions=1, best=None):
        self.population = data["population"]
        self.fitness = data["fitness"]
        self.func = func
        self.interval = interval
        self.fps = fps
        self.filename = filename
        self.dimensions = dimensions
        self.best = best
    
    def animate_growth(self):
        if self.dimensions == 1:
            self.__1d_animate_growth__()
        elif self.dimensions == 2:
            self.__2d_animate_growth__()
        else:
            print("Too many dimensions")

    def fitness_trend(self):
        #fitness = np.array(self.fitness)
        #fitness = fitness.T

        fig = plt.figure()
        #for i in range(len(fitness)):
            #print(min(fitness[i]), i)
            #plt.scatter(i, min(fitness[i]))
        minf = []
        for i in self.fitness:
            minf.append(min(i))
        plt.plot(self.best)

        # Add labels and title
        plt.xlabel('Epoch')
        plt.ylabel('Fitness')
        plt.title('Fitness of population')
        plt.savefig(f'fitness_trend_{self.filename}.png')
        plt.close(fig)
        
    def distances(self):
        #best_fitness =  np.array([self.func(*args) for args in self.best])

        fig = plt.figure()
        distance = np.diff(self.best)
        distance = [abs(i) for i in distance]

        # Plot the differences
        plt.plot(distance)

        # Add labels and title
        plt.xlabel('Epoch')
        plt.ylabel('Distance')
        plt.title('Distance between min values')
        plt.savefig(f'distances_{self.filename}.png')
        plt.close(fig)


    def __1d_animate_growth__(self):
        def plot_growth(i):
            fig, ax = plt.subplots(figsize=(10,5))
            # Plot population
            x_population = self.population[i][0]
            y_fitness = self.fitness[i]
            ax.plot(x_population, y_fitness, 'bo', label='Fitness')
            
            # Plot harmonic function
            x_smooth = np.linspace(self.interval[0], self.interval[1], 300)
            y_smooth = self.func(x_smooth)
            ax.plot(x_smooth, y_smooth, 'r-', label=f'{self.filename} Function')
            
            ax.set_title('Epoch {}'.format(i+1))
            ax.set_xlabel('Population')
            ax.set_ylabel('Fitness')

            fig.canvas.draw()       # draw the canvas, cache the renderer
            image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
            image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            plt.close(fig)
            return image

        imageio.mimsave(f'./animated_{self.filename}.gif', [plot_growth(i) for i in range(len(self.population))], fps=self.fps)
    
    def __2d_animate_growth__(self):
        def plot_growth(i):
            fig = plt.figure(figsize=(35, 10))
            fig.suptitle('Epoch {}'.format(i),  x=0.42, y=0.95)
            ax = fig.add_subplot(111, projection='3d')

            # Access population data for the i-th iteration
            x_population = self.population[i][0]
            y_population = self.population[i][1]
            z_fitness = self.fitness[i]

            # Plot population
            ax.scatter(x_population, y_population, zs=z_fitness, c='r', label='Fitness')

            # Plot 3D function surface
            x = np.linspace(self.interval[0][0], self.interval[0][1], 100)
            y = np.linspace(self.interval[1][0], self.interval[1][1], 100)
            X, Y = np.meshgrid(x, y)
            Z = self.func(X, Y)
            ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)

            ax.set_xlabel('Population - x')
            ax.set_ylabel('Population - y')
            ax.set_zlabel('Fitness')
            ax.legend()


            # Change the viewing angle
            ax.view_init(elev=73, azim=0)   
            ax = fig.add_subplot(121, projection='3d')   
            ax.scatter(x_population, y_population, zs=z_fitness, c='r', label='Fitness')   
            ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)

            ax.set_xlabel('Population - x')
            ax.set_ylabel('Population - y')
            ax.set_zlabel('Fitness')
            ax.legend()


            # Convert the plot to an image
            fig.canvas.draw()
            image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
            image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            image =  image[:, 680:2200, :]
            plt.close(fig)  # Close the figure to prevent memory leak
            return image

        # Generate GIF from plots
        imageio.mimsave(f'./animated_{self.filename}.gif', [plot_growth(i) for i in range(len(self.population))], fps=self.fps)

