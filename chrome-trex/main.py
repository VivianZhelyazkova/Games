import pygame
import os
from t_rex import Trex
from clouds import Cloud
from background import Background

pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
GAME_SPEED = 15

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    global points
    run = True
    clock = pygame.time.Clock()
    trex = Trex()
    cloud = Cloud(SCREEN_WIDTH, GAME_SPEED)
    background = Background(GAME_SPEED)
    font = pygame.font.Font("freesansbold.ttf", 30)
    points = 0
    obstacles = []

    def callback(obstacle):
        obstacles.remove(obstacle)

    def score():
        global points
        text = font.render(f"POINTS: {points}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 30)
        SCREEN.blit(text, text_rect)
        points += 1

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
        background.draw(SCREEN)
        background.update()
        score()
        clock.tick(30)
        pygame.display.update()


main()
