import pygame, random
from Config import *

class Shark:
    def __init__(self):

        self.speed = random.randint(3,10)

        self.opacity=255

        #image loading
        self.image = pygame.image.load(SHARK_PATHS).convert_alpha()
        self.image_right = self.image
        self.image_left = pygame.transform.flip(self.image, True, False)
        self.current_image = self.image_right

        #create rectangle
        self.rect = self.image.get_rect()
        random_y = random.randint(0, HEIGHT - self.rect.height)
        self.rect.midleft =(WIDTH, random_y)
        self.direction=1
        self.moving_off_screen=False
        #Spawn sound
        self.spawn_sound = pygame.mixer.Sound(SHARK_SOUND)
        self.spawn_sound.play()

        self.creation_time = pygame.time.get_ticks()
        self.lifespan = 10000

    def move(self):
        if not self.moving_off_screen:
            self.rect.x += self.speed * self.direction
            if self.rect.right >= WIDTH:
               self.current_image = self.image_left
               self.direction = -1
            elif self.rect.left <= 0:
               self.current_image = self.image_right
               self.direction = 1
        else:
            self.rect.x += self.speed


    #define creative asset for Food
    def draw(self,surface):
        current_time = pygame.time.get_ticks()
        if current_time - self.creation_time > self.lifespan:
            return False
        SCREEN.blit(self.current_image, self.rect)
        return  True

