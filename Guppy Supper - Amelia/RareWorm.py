from Config import *
import pygame, random
import math

class RareWorm:
    def __init__(self):

        #wprm types
        self.types = random.choice(list(RARE_WORM_SPEED.keys()))

        #worm speed by type
        self.speed = RARE_WORM_SPEED[self.types]

        #image loading
        sprite_choice = random.choice(RARE_WORM_PATH[self.types])
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
        self.original_x = random.randint(0, WIDTH - self.rect.width)
        self.time = 0
        self.amplitude = 50

    #define worm falling
    def fall(self):
        self.time += 0.1
        # Move down
        self.rect.y += self.speed
        # Move side to side in a sine wave
        self.rect.x = int(self.original_x + math.sin(self.time) * self.amplitude)

    #define creative asset for worm
    def draw(self,surface):
        surface.blit(self.sprite, self.rect)