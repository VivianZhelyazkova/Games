import os
import pygame
import random

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]


class Obstacle:

    def __init__(self, image, obst_type, screen_width, game_speed, callback):
        self.image = image
        self.obst_type = obst_type
        self.rect = self.image[self.obst_type].get_rect()
        self.rect.x = screen_width
        self.game_speed = game_speed
        self.callback = callback

    def update(self):
        self.rect.x -= self.game_speed
        if self.rect.x < - self.rect.width:
            self.callback(self)

    def draw(self, screen):
        screen.blit(self.image[self.obst_type], self.rect)


class LargeCactus(Obstacle):

    def __init__(self, screen_width, game_speed, callback):
        self.obst_type = random.randint(0, 2)
        super().__init__(LARGE_CACTUS, self.obst_type, screen_width, game_speed, callback)
        self.rect.y = 300


class SmallCactus(Obstacle):

    def __init__(self, screen_width, game_speed, callback):
        self.obst_type = random.randint(0, 2)
        super().__init__(SMALL_CACTUS, self.obst_type, screen_width, game_speed, callback)
        self.rect.y = 325


class Bird(Obstacle):

    def __init__(self, screen_width, game_speed, callback):
        self.obst_type = 0
        super().__init__(BIRD, self.obst_type, screen_width, game_speed, callback)
        self.rect.y = 250
        self.step_index = 0

    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1
