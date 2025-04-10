import pygame, random
from Config import *

#define class Meteor
class Meteor:
    def __init__(self):

        #meteor types
        self.types = random.choice(list(METEOR_SPEEDS.keys()))

        #meteor speed by type
        self.speed = METEOR_SPEEDS[self.types]

        #image loading
        sprite_choice = random.choice(PATHS[self.types])
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

    #define meteor falling
    def fall(self):
        self.rect = self.rect.move(0, self.speed)

    #define creative asset for Meteor
    def draw(self,surface):
        surface.blit(self.sprite, self.rect)