import math

class Creature:
    def __init__(self, location):
        self.location = location

        self.movement_speed = 5
        self.rotation_speed = 0.5

        self.rotation = 0.0    # Radians, not bound
        self.size = 10

    # Amount ranges from 0 to 1
    def move(self, amount):
        self.location[0] += amount * math.cos(self.rotation) * self.movement_speed
        self.location[1] += amount * math.sin(self.rotation) * self.movement_speed

    # Amount ranges from 0 to 1
    def rotate(self, amount):
        self.rotation += amount * self.rotation_speed

    # Returns list of points.
    def draw(self):
        rotations = [
            0,
            2/3 * math.pi,
            math.pi,
            4/3 * math.pi
        ]

        points = []

        for rot in rotations:
            points.append([
                self.location[0] + self.size * math.cos(self.rotation + rot),
                self.location[1] + self.size * math.sin(self.rotation + rot)
            ])

        return points
