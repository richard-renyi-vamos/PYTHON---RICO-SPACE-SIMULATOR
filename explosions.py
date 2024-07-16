# explosion.py

import pygame
import random

class Particle:
    def __init__(self, x, y, size, color, x_vel, y_vel):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.x_vel = x_vel
        self.y_vel = y_vel

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.size -= 0.1  # Shrink over time

    def draw(self, screen):
        if self.size > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

class Explosion:
    def __init__(self, x, y, color):
        self.particles = []
        for _ in range(20):  # Number of particles
            size = random.randint(2, 6)
            x_vel = random.uniform(-2, 2)
            y_vel = random.uniform(-2, 2)
            self.particles.append(Particle(x, y, size, color, x_vel, y_vel))

    def update(self):
        self.particles = [p for p in self.particles if p.size > 0]
        for particle in self.particles:
            particle.move()

    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
