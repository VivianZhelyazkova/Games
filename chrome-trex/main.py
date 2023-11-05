import pygame
import os
from t_rex import Trex
from clouds import Cloud

pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
GAME_SPEED = 15

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]




def main():
    run = True
    clock = pygame.time.Clock()
    trex = Trex()
    cloud = Cloud(SCREEN_WIDTH, GAME_SPEED)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()
        cloud.draw(SCREEN)
        cloud.update()
        trex.draw(SCREEN)
        trex.update(user_input)
        clock.tick(30)
        pygame.display.update()


main()
