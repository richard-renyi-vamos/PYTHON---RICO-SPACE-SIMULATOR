import pygame
import sys
import random
import tkinter as tk
from tkinter import ttk

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Simulator")

# Load images
background = pygame.image.load("space.jpg")
background = pygame.transform.scale(background, (width, height))
spaceship_img = pygame.image.load("spaceship.png")
spaceship_img = pygame.transform.scale(spaceship_img, (40, 40))  # Adjust size as needed

# Set up font for timer
font = pygame.font.Font(None, 36)

# Star settings
star_count = 100
star_speed = 2
star_size = 2

# Star class
class Star:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.speed = random.uniform(0.5, 1.5) * star_speed
        self.size = random.randint(1, star_size)

    def move(self):
        self.y += self.speed
        if self.y > height:
            self.y = 0
            self.x = random.randint(0, width)

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.size)

# Create stars
stars = [Star() for _ in range(star_count)]

# Spaceship class
class Spaceship:
    def __init__(self):
        self.image = spaceship_img
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.speed = 5

    def move(self, dx, dy):
        self.rect.x = max(0, min(width - self.rect.width, self.rect.x + dx * self.speed))
        self.rect.y = max(0, min(height - self.rect.height, self.rect.y + dy * self.speed))

    def draw(self):
        screen.blit(self.image, self.rect)

# Create spaceship
spaceship = Spaceship()

# GUI class
class SettingsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Star Animation Settings")

        ttk.Label(master, text="Star Count:").grid(row=0, column=0, padx=5, pady=5)
        self.star_count_entry = ttk.Entry(master)
        self.star_count_entry.grid(row=0, column=1, padx=5, pady=5)
        self.star_count_entry.insert(0, str(star_count))

        ttk.Label(master, text="Star Speed:").grid(row=1, column=0, padx=5, pady=5)
        self.star_speed_entry = ttk.Entry(master)
        self.star_speed_entry.grid(row=1, column=1, padx=5, pady=5)
        self.star_speed_entry.insert(0, str(star_speed))

        ttk.Label(master, text="Star Size:").grid(row=2, column=0, padx=5, pady=5)
        self.star_size_entry = ttk.Entry(master)
        self.star_size_entry.grid(row=2, column=1, padx=5, pady=5)
        self.star_size_entry.insert(0, str(star_size))

        ttk.Button(master, text="Apply", command=self.apply_settings).grid(row=3, column=0, columnspan=2, pady=10)

    def apply_settings(self):
        global star_count, star_speed, star_size, stars
        star_count = int(self.star_count_entry.get())
        star_speed = float(self.star_speed_entry.get())
        star_size = int(self.star_size_entry.get())
        stars = [Star() for _ in range(star_count)]

# Create GUI window
root = tk.Tk()
gui = SettingsGUI(root)

# Main game loop
clock = pygame.time.Clock()
running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle spaceship movement
    keys = pygame.key.get_pressed()
    dx = keys[pygame.K_d] - keys[pygame.K_a]
    dy = keys[pygame.K_s] - keys[pygame.K_w]
    spaceship.move(dx, dy)

    # Update star positions
    for star in stars:
        star.move()

    # Draw background, stars, and spaceship
    screen.blit(background, (0, 0))
    for star in stars:
        star.draw()
    spaceship.draw()

    # Calculate and display timer
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert to seconds
    timer_text = font.render(f"SPACE TRIP DURATION: {elapsed_time}s", True, (255, 255, 255))
    timer_rect = timer_text.get_rect()
    timer_rect.topright = (width - 10, 10)
    screen.blit(timer_text, timer_rect)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

    # Update GUI
    root.update()

# Quit Pygame and Tkinter
pygame.quit()
root.destroy()
sys.exit()
