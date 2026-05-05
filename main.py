import pygame
import map
from creature import *


# Color constants
GRASS = (19,133,16)
SAND = (246,215,176)
ICE = (214, 255, 250)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (150, 150, 150)
WHITE = (255, 255, 255)

# Screen constants
SCREEN_SIZE = (800, 800)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

# Map setup
food_value = 25
game_map = map.Map(SCREEN_SIZE, food_value)

creature = Creature([400, 400])

if __name__ == '__main__':

    # Grow food
    game_map.random_grow(5)

    while running:

        # Handles closing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Create background
        screen.fill(DARK_GRAY)

        # Show food
        for food in game_map.food:
            pygame.draw.circle(screen, GREEN, food.location, food.value)

        # Show creature
        pts = creature.draw()

        for pt in pts:
            pygame.draw.circle(screen, BLUE, (pt[0], pt[1]), 1)

        # Tick game
        pygame.display.flip()
        clock.tick(60)