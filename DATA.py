import math

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