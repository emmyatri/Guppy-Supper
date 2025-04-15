import pygame, random
from Config import *

#define class Meteor
class FOOD:
    def __init__(self):

        #Food types
        self.types = random.choice(list(FOOD_SPEEDS.keys()))

        #Food speed by Level
        self.speed = FOOD_SPEEDS[self.types]

        #image loading
        self.sprite = pygame.image.load(FOOD_IMAGE).convert_alpha()

        #create rectangle
        self.rect = self.sprite.get_rect()

        #Spawn sound
        self.spawn_sound = pygame.mixer.Sound(FOOD_APPEAR)

        #spawn location
        screen_width = WIDTH
        screen_height = HEIGHT
        random_x = random.randint(0, screen_width - self.rect.width)
        random_y = random.randint(0, screen_height - self.rect.height)
        self.rect.topleft = (random_x, random_y)


    #define creative asset for Food
    def draw(self,surface):
        surface.blit(self.sprite, self.rect)