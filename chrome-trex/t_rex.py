import pygame
import os

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = [pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))]
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]


class Trex:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 10

    def __init__(self):
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.duck_img = DUCKING
        self.is_running = True
        self.is_jumping = False
        self.is_ducking = False
        self.step_index = 0
        self.img = self.run_img[0]
        self.hit_box = self.img.get_rect()
        self.hit_box.x = Trex.X_POS
        self.hit_box.y = Trex.Y_POS

    def update(self, user_input):
        if self.is_running:
            self.run()
        if self.is_jumping:
            self.jump()
        if self.is_ducking:
            self.duck()
        if self.step_index >= 10:
            self.step_index = 0
        if user_input[pygame.K_UP] and not self.is_jumping:
            self.is_running = False
            self.is_ducking = False
            self.is_jumping = True
        elif user_input[pygame.K_DOWN] and not self.is_jumping:
            self.is_running = False
            self.is_ducking = True
            self.is_jumping = False
        elif not (self.is_jumping or user_input[pygame.K_DOWN]):
            self.is_running = True
            self.is_ducking = False
            self.is_jumping = False

    def run(self):
        self.img = self.run_img[self.step_index // 5]
        self.hit_box = self.img.get_rect()
        self.hit_box.x = Trex.X_POS
        self.hit_box.y = Trex.Y_POS
        self.step_index += 1

    def jump(self):
        pass


    def duck(self):
        self.img = self.duck_img[self.step_index // 5]
        self.hit_box = self.img.get_rect()
        self.hit_box.x = Trex.X_POS
        self.hit_box.y = Trex.Y_POS_DUCK
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.img, (self.hit_box.x, self.hit_box.y))
