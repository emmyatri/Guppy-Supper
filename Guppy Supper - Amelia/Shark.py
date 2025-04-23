import pygame, random
from Config import *

class Shark:
    def __init__(self):

        self.speed = random.randint(3,10)

        self.opacity=255

        #image loading
        self.image = pygame.image.load(SHARK_PATHS).convert_alpha()

        #create rectangle
        self.rect = self.image.get_rect()
        self.rect.midleft =(0,random.randint(0, HEIGHT-self.rect.height))
        self.direction=1
        self.moving_off_screen=False
        #Spawn sound
        self.spawn_sound = pygame.mixer.Sound(SHARK_SOUND)
        self.spawn_sound.play()


    def move(self):
        if not self.moving_off_screen:
            self.rect.x += self.speed * self.direction
            if self.rect.right >= WIDTH:
               self.direction = -1
            elif self.rect.left <= 0:
               self.direction = 1
        else:
            self.rect.x += self.speed


    #define creative asset for Food
    def draw(self,surface):
        self.image.set_alpha(self.opacity)
        surface.blit(self.image, self.rect)
        return  True

