import pygame
from pygame.locals import *
import time

# Initialize pygame
pygame.init()

# Create a blank window of width 600 pixels and height 600 pixels.
screen = pygame.display.set_mode((600, 600))

# Set the name of our window to "Shapes"
pygame.display.set_caption("Shapes")

color = (255, 255, 255)
dragging = False
circle_pos = (0, 0)
circle_radius = 20

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            dragging = True
            circle_pos = event.pos
        elif event.type == MOUSEBUTTONUP:
            dragging = False
        elif event.type == MOUSEMOTION and dragging:
            circle_pos = event.pos
        elif event.type == QUIT:
            pygame.quit()
            exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the circle
    pygame.draw.circle(screen, color, circle_pos, circle_radius)

    # Update the display
    pygame.display.update()