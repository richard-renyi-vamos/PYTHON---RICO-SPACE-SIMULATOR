import pygame

class Spaceship:
    def __init__(self, image_path, screen_width, screen_height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (40, 40))  # Adjust size as needed
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 5

    def move(self, dx, dy, screen_width, screen_height):
        self.rect.x = max(0, min(screen_width - self.rect.width, self.rect.x + dx * self.speed))
        self.rect.y = max(0, min(screen_height - self.rect.height, self.rect.y + dy * self.speed))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
