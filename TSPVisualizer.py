import matplotlib.pyplot as plt
import numpy as np
import imageio

class Visualizer:
    def __init__(self, points, paths, fps=10, filename="f"):
        self.points = points
        self.paths = paths
        self.fps = fps
        self.filename = filename

    def __1d_animate_growth__(self):
        def plot_growth(j):
            fig = plt.figure(figsize=(8, 6))
            plt.scatter(self.points[:,0], self.points[:,1], c='r', marker='o')
                
            n_points = len(self.points)
            for i in range(n_points-1):
                plt.plot([self.points[self.paths[j][i],0], self.points[self.paths[j][i+1],0]],
                            [self.points[self.paths[j][i],1], self.points[self.paths[j][i+1],1]],
                            c='g', linestyle='-', linewidth=2, marker='o')
                    
            plt.plot([self.points[self.paths[j][0],0], self.points[self.paths[j][-1],0]],
                        [self.points[self.paths[j][0],1], self.points[self.paths[j][-1],1]],
                        c='g', linestyle='-', linewidth=2, marker='o')
                
            plt.title('Epoch {}'.format(j+1))

            fig.canvas.draw()       
            image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
            image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            plt.close(fig)
            return image

        imageio.mimsave(f'./animated_{self.filename}.gif', [plot_growth(i) for i in range(len(self.paths))], fps=10)