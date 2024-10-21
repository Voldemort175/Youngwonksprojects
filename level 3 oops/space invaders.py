import random
import time
import pygame

from pygame.locals import *
# Initialize pygame
pygame.init()

# Create a blank window of width 600 pixels and height 600 pixels.
screen = pygame.display.set_mode((600, 600))

class Character:
    def __init__(self, image_path, length, width):
        self.x = 300
        self.y = 100
        self.length = length
        self.width = width
        self.image = pygame.transform.scale(pygame.image.load(image_path), (length, width))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Alien(Character):
    def __init__(self, x, y):
        image_path = random.choice([
            r"D:\Study Stuff\Wonksknow\level 3 oops\alien1.png",
            r"D:\Study Stuff\Wonksknow\level 3 oops\alien2.png",
            r"D:\Study Stuff\Wonksknow\level 3 oops\alien3.png"
        ])
        super().__init__(image_path, 50, 80)
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = "right"

    def move_alien(self):
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed

        if self.x >= 600 or self.x <= 0:
            self.direction = "left" if self.direction == "right" else "right"
            self.y += 50  # Move down by 50 pixels

aliens = []
for i in range(5):  # 5 rows
    row = []
    for j in range(10):  # 10 columns
        alien = Alien(j * 50, i * 50)  # spacing between aliens
        row.append(alien)
    aliens.append(row)

direction = "right"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))  # Clear the screen

    for row in aliens:
        for alien in row:
            alien.draw()
            if direction == "right":
                alien.x += 10
            elif direction == "left":
                alien.x -= 10

            if alien.x >= 600 or alien.x <= 0:
                direction = "left" if direction == "right" else "right"
                alien.y += 50  # Move down by 50 pixels

    pygame.display.update()
    time.sleep(0.1)  # Add a small delay to control the frame rate