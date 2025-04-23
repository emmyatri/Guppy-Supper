import pygame, random
from Config import *

#define class Meteor
class OBSTACLE:
    def __init__(self,image,start_time):

        #Food speed by Level
        self.speed = random.randint(3,10)

        self.start_time = start_time
        self.opacity=255

        #image loading
        self.sprite = pygame.image.load(SHARK_PATHS).convert_alpha()
        self.sprite = pygame.image.load(ROCK_OBSTACLE).convert_alpha()
        #create rectangle
        self.rect = self.sprite.get_rect()
        self.rect.topleft=(random.randint(0, WIDTH-self.rect.width),0)

        #Spawn sound
        self.spawn_sound = pygame.mixer.Sound(FOOD_APPEAR)


    def fall(self):
       self.rect.y += self.speed


    #define creative asset for Food
    def draw(self,surface):
        elapsed_time = pygame.time.get_ticks() - self.start_time/1000
        if elapsed_time <= 5:
            self.opacity=64
        if elapsed_time <= 10:
            self.opacity=128
        elif elapsed_time <= 15:
            self.opacity=255
        else:
            OBSTACLE.remove(self)
            return
        self.sprite.set_alpha(self.opacity)
        surface.blit(self.sprite, self.rect)