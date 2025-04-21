import pygame, sys, Config
from pygame.sprite import collide_rect

from Config import *

#define class player
class Player:
    def __init__(self):
        self.speed = PLAYER_SPEED
        self.sprite = pygame.image.load(PLAYER_IMAGE)
        self.rect = self.sprite.get_rect()
        self.rect.center = ((RESOLUTION[0]/2)-(self.rect.width/2),(RESOLUTION[1]/2)-(self.rect.height/2))
        self.alive = True
        self.deadSound = pygame.mixer.Sound(PLAYER_DEATH_SOUND)

    #defining player movement
    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.rect.left > 0:
                self.rect = self.rect.move (-5,0)
        if keys[pygame.K_w]:  # check w is being pressed.
            if self.rect.top > 0:
                self_rect = self.rect.move(0, -5)  # move the player
        if keys[pygame.K_s]: # check if s is pressed
            if self.rect.bottom > (RESOLUTION[1] - 100):
                self_rect =self.rect.move(0, 5)  # move the player
        if keys[pygame.K_d]:
            if self.rect.right < WIDTH:
                self.rect = self.rect.move (5,0)
    def eat(self,FOOD_BLIP):
        if self.rect.colliderect(FOOD_BLIP):
            global SCORE
            SCORE+=10


    #define creative asset for Player
    def draw(self):
        SCREEN.blit(self.sprite, self.rect)