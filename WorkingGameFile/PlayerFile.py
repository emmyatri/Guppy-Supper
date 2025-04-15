import pygame, sys
from Config import *

#define class player
class Player:
    def __init__(self):
        self.speed = PLAYER_SPEED
        self.sprite = pygame.image.load(PLAYER_IMAGE)
        self.rect = self.sprite.get_rect()
        self.rect.midbottom = (WIDTH//2, HEIGHT -150)
        self.alive = True
        self.deadSound = pygame.mixer.Sound(PLAYER_DEATH_SOUND)

    #defining player movement
    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.x -= self.speed

        if keys[pygame.K_d]:
            if self.rect.right < WIDTH:
                self.rect.x += self.speed

        if keys[pygame.K_w]:
            if self.rect.top > 0:
                self.rect.y -= self.speed

        if keys[pygame.K_s]:
            if self.rect.bottom < HEIGHT :
                self.rect.y += self.speed

    #define creative asset for Player
    def draw(self):
        SCREEN.blit(self.sprite, self.rect)