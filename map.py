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

    def grow_food(self, location, radius, amount):
        for _ in range(amount):

            # Get food location and offset it
            x = location[0] + (random.random() - 0.5) * radius
            y = location[1] + (random.random() - 0.5) * radius

            # Clamp location to bounds
            x = min(self.bounds[0], max(x, 0))
            y = min(self.bounds[1], max(y, 0))

            self.food.append(Food(
                (x, y),
                self.food_value / amount
            ))