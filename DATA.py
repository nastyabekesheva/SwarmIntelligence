import math
import random

class CircleDotsGenerator:
    def __init__(self, radius=1, n=10):
        self.radius = radius
        self.n = n

    def generate_dots(self):
        if self.n <= 0:
            return []

        angle_step = 2 * math.pi / self.n
        dots = []

        for i in range(self.n):
            x = self.radius * math.cos(i * angle_step)
            y = self.radius * math.sin(i * angle_step)
            dots.append((x, y))

        return dots

class KnapsackGenerator:
    def __init__(self, num_items, capacity):
        self.num_items = max(20, num_items)
        self.capacity = capacity

    def generate_data(self):
        weights = []
        total_weight = 0
        while total_weight <= self.capacity:
            weight = random.randint(1, 20)  
            if total_weight + weight > self.capacity:
                break
            weights.append(weight)
            total_weight += weight

        values = [random.randint(1, 50) for _ in range(len(weights))]  
        return weights, values

