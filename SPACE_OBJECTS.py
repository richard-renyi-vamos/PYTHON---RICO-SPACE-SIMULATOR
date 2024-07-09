import pygame
import random

# Constants
width, height = 800, 600

class SpaceObject:
    def __init__(self, speed_range, size_range):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.speed = random.uniform(*speed_range)
        self.size = random.randint(*size_range)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.shape = random.choice(['circle', 'square'])

    def move(self):
        self.y += self.speed
        if self.y > height:
            self.y = 0
            self.x = random.randint(0, width)

    def draw(self, screen):
        if self.shape == 'circle':
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        elif self.shape == 'square':
            pygame.draw.rect(screen, self.color, (int(self.x), int(self.y), self.size, self.size))
