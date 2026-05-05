import random

class Food:
    def __init__(self, location, value):
        self.location = location
        self.value = value

class Map:
    def __init__(self, bounds, food_value):
        self.bounds = bounds

        self.food_value = food_value
        self.food = []

    def random_grow(self, amount, divide=True):
        for _ in range(amount):

            # Create location
            x = random.random() * self.bounds[0]
            y = random.random() * self.bounds[1]

            value = self.food_value
            if divide:
                value /= amount

            self.food.append(Food(
                (x, y),
                value
            ))

    def local_grow(self, location, radius, amount, divide=True):
        for _ in range(amount):

            # Get food location and offset it
            x = location[0] + (random.random() - 0.5) * radius
            y = location[1] + (random.random() - 0.5) * radius

            # Clamp location to bounds
            x = min(self.bounds[0], max(x, 0))
            y = min(self.bounds[1], max(y, 0))

            value = self.food_value
            if divide:
                value /= amount

            self.food.append(Food(
                (x, y),
                value
            ))