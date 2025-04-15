import pygame, random
from Config import *

#define class Worm
class Worm:
    def __init__(self):

        #wprm types
        self.types = random.choice(list(WORM_SPEED.keys()))

        #worm speed by type
        self.speed = WORM_SPEED[self.types]

        #image loading
        sprite_choice = random.choice(WORM_PATHS[self.types])
        self.sprite = pygame.image.load(sprite_choice).convert_alpha()

        #create rectangle
        self.rect = self.sprite.get_rect()

        #random spawn sound
        rand_sound = random.choice(SOUNDS)
        self.spawn_sound = pygame.mixer.Sound(rand_sound)

        #spawn location
        screen_width = WIDTH
        random_x = random.randint(0, screen_width - self.rect.width)
        self.rect.topleft = (random_x, 0)

    #define worm falling
    def fall(self):
        self.rect = self.rect.move(0, self.speed)

    #define creative asset for worm
    def draw(self,surface):
        surface.blit(self.sprite, self.rect)