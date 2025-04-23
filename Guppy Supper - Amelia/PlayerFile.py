import pygame, sys
from Config import *

#define class player
class Player:
    def __init__(self):
        self.speed = PLAYER_SPEED
        self.sprite = pygame.image.load(PLAYER_IMAGE)
        self.sprite_left=self.sprite
        self.sprite_right=pygame.transform.flip(self.sprite,True,False)
        self.current_sprite=self.sprite_left
        self.rect = self.sprite.get_rect()
        self.rect.midbottom = (WIDTH//2, HEIGHT -150)
        self.alive = True
        self.deadSound = pygame.mixer.Sound(PLAYER_DEATH_SOUND)

    #defining player movement
    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= self.speed
            self.current_sprite=self.sprite_left

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self.rect.right < WIDTH:
                self.rect.x += self.speed
                self.current_sprite=self.sprite_right

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.rect.top > 0:
                self.rect.y -= self.speed

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if self.rect.bottom < HEIGHT :
                self.rect.y += self.speed

    #define creative asset for Player
    def draw(self):
        SCREEN.blit(self.current_sprite, self.rect)