import os
import pygame
import random

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))


class Cloud:

    def __init__(self, screen_width, game_speed):
        self.image = CLOUD
        self.x = screen_width + random.randint(500, 800)
        self.y = random.randint(80, 350)
        self.width = self.image.get_width()
        self.speed = game_speed
        self.screen_width = screen_width

    def update(self):
        self.x -= self.speed
        if self.x < - self.width:
            self.x = self.screen_width + random.randint(500, 800)
            self.y = random.randint(80, 350)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
