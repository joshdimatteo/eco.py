import pygame
import map


# Color constants
GRASS = (19,133,16)
SAND = (246,215,176)
ICE = (214, 255, 250)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

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

if __name__ == '__main__':

    # Grow food
    game_map.grow_food((250, 250), 100, 5)

    while running:

        # Handles closing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Create background
        screen.fill(GRASS)

        # Show food
        for food in game_map.food:
            pygame.draw.circle(screen, GREEN, food.location, food.value)

        # Tick game
        pygame.display.flip()
        clock.tick(60)