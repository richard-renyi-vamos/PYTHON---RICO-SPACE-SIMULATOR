import sys
import os
import pygame
import random
import tkinter as tk
from tkinter import ttk
from SPACE_OBJECTS import SpaceObject  # Import the new SpaceObject class
from SPACESHIP import Spaceship  # Import the Spaceship class

# Ensure the script can find the modules in the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer for music

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Simulator")

# Load images
background_path = os.path.join(script_dir, "space.jpg")
spaceship_image_path = os.path.join(script_dir, "spaceship.png")

background = pygame.image.load(background_path)
background = pygame.transform.scale(background, (width, height))

# Load and play music
music_path = os.path.join(script_dir, "Starry Dream.mp3")
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)  # -1 means loop indefinitely
music_playing = True

# Set up font for timer
font = pygame.font.Font(None, 36)

# Space object settings
space_object_count = 100
speed_range = (0.5, 3.0)
size_range = (1, 5)

# Create space objects
space_objects = [SpaceObject(speed_range, size_range) for _ in range(space_object_count)]

# Create spaceship
spaceship = Spaceship(spaceship_image_path, width, height)

# GUI class
class SettingsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Space Object Animation Settings")

        ttk.Label(master, text="Space Object Count:").grid(row=0, column=0, padx=5, pady=5)
        self.count_entry = ttk.Entry(master)
        self.count_entry.grid(row=0, column=1, padx=5, pady=5)
        self.count_entry.insert(0, str(space_object_count))

        ttk.Label(master, text="Speed Range (min, max):").grid(row=1, column=0, padx=5, pady=5)
        self.speed_min_entry = ttk.Entry(master)
        self.speed_min_entry.grid(row=1, column=1, padx=5, pady=5)
        self.speed_min_entry.insert(0, str(speed_range[0]))
        self.speed_max_entry = ttk.Entry(master)
        self.speed_max_entry.grid(row=1, column=2, padx=5, pady=5)
        self.speed_max_entry.insert(0, str(speed_range[1]))

        ttk.Label(master, text="Size Range (min, max):").grid(row=2, column=0, padx=5, pady=5)
        self.size_min_entry = ttk.Entry(master)
        self.size_min_entry.grid(row=2, column=1, padx=5, pady=5)
        self.size_min_entry.insert(0, str(size_range[0]))
        self.size_max_entry = ttk.Entry(master)
        self.size_max_entry.grid(row=2, column=2, padx=5, pady=5)
        self.size_max_entry.insert(0, str(size_range[1]))

        ttk.Button(master, text="Apply", command=self.apply_settings).grid(row=3, column=0, columnspan=3, pady=10)

        # Music toggle button
        self.music_button = ttk.Button(master, text="Music: ON", command=self.toggle_music)
        self.music_button.grid(row=4, column=0, columnspan=3, pady=10)

    def apply_settings(self):
        global space_object_count, speed_range, size_range, space_objects
        space_object_count = int(self.count_entry.get())
        speed_range = (float(self.speed_min_entry.get()), float(self.speed_max_entry.get()))
        size_range = (int(self.size_min_entry.get()), int(self.size_max_entry.get()))
        space_objects = [SpaceObject(speed_range, size_range) for _ in range(space_object_count)]

    def toggle_music(self):
        global music_playing
        if music_playing:
            pygame.mixer.music.pause()
            self.music_button.config(text="Music: OFF")
            music_playing = False
        else:
            pygame.mixer.music.unpause()
            self.music_button.config(text="Music: ON")
            music_playing = True

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
    dx = keys[pygame.K_d] - keys[pygame.K_a] + keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    dy = keys[pygame.K_s] - keys[pygame.K_w] + keys[pygame.K_DOWN] - keys[pygame.K_UP]
    spaceship.move(dx, dy, width, height)

    # Update space object positions
    for space_object in space_objects:
        space_object.move()

    # Draw background, space objects, and spaceship
    screen.blit(background, (0, 0))
    for space_object in space_objects:
        space_object.draw(screen)
    spaceship.draw(screen)

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
