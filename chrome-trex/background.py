import os
import pygame

BACKGROUND = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


class Background:

    def __init__(self, game_speed):
        self.image = BACKGROUND
        self.width = self.image.get_width()
        self.game_speed = game_speed
        self.x = 0
        self.y = 380

    def update(self):
        self.x -= self.game_speed
        if self.x <= -self.width:
            self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x + self.width, self.y))
