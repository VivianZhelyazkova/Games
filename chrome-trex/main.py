import pygame
import os
from t_rex import Trex
from clouds import Cloud
from background import Background
import random
from obstacle import *

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
    death_count = 0

    def callback(obstacle):
        obstacles.remove(obstacle)

    def score():
        global points
        text = font.render(f"POINTS: {points}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (900, 30)
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
        if len(obstacles) == 0:
            current_obstacle = random.randint(0, 2)
            if current_obstacle == 0:
                obstacles.append(SmallCactus(SCREEN_WIDTH, GAME_SPEED, callback))
            elif current_obstacle == 1:
                obstacles.append(LargeCactus(SCREEN_WIDTH, GAME_SPEED, callback))
            elif current_obstacle == 2:
                obstacles.append(Bird(SCREEN_WIDTH, GAME_SPEED, callback))
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if trex.hit_box.colliderect(obstacle.rect):
                death_count += 1
                menu(death_count)

        score()
        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font("freesansbold.ttf", 30)
        if death_count == 0:
            head = font.render(f"Press any key to start:", True, (0, 0, 0))
        elif death_count > 0:
            head = font.render(f"GAME OVER", True, (0, 0, 0))
            body = font.render(f"Your score is: {points}", True, (0, 0, 0))
            body_rect = body.get_rect()
            body_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(body, body_rect)
        head_rect = head.get_rect()
        head_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(head, head_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(0)
