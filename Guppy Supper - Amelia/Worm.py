import pygame, random
from Config import *
import math

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
        self.original_x = random_x
        self.time = 0
        self.amplitude = 50
        self.frequency = 0.1

    #define worm falling
    def fall(self):
        # Move down
        self.rect.y += self.speed

        # bounded time
        self.time = (self.time + self.frequency) % (2 * math.pi)

        # Move side to side in a sine wave
        self.rect.x = int(self.original_x + math.sin(self.time) * self.amplitude)

    #define creative asset for worm
    def draw(self,surface):
        surface.blit(self.sprite, self.rect)