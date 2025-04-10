import pygame, sys
pygame.init()
pygame.mixer.init()

#general settings
##################################
WIDTH, HEIGHT = 480,800
RESOLUTION = (WIDTH, HEIGHT)
FPS = 60
SCREEN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_mode(RESOLUTION)

CLOCK = pygame.time.Clock()
CLOCK.tick(60)

#custom meteor event
METEOR_EVENT = pygame.USEREVENT + 1

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#player settings
##################################
PLAYER_SPEED = 12
PLAYER_IMAGE = "img1/player_sprite.png"
PLAYER_DEATH_SOUND = "audio1/player_dead.ogg"

#meteor settings
##################################
METEOR_SPEEDS = {
    "big" : 10,
    "medium" : 11,
    "small" : 12,
    "tiny" : 12
}


# Creative assets for player/meteor/background
##################################

PATHS = {
    "big" : ["img1/meteor_big_1.png", "img1/meteor_big_2.png", "img1/meteor_big_3.png", "img1/meteor_big_4.png"],
    "medium" : ["img1/meteor_med_1.png", "img1/meteor_med_2.png"],
    "small" : ["img1/meteor_small_1.png", "img1/meteor_small_2.png"],
    "tiny" : ["img1/meteor_tiny_1.png", "img1/meteor_tiny_2.png"]
}

SOUNDS = ["audio1/spawn_sound_1.ogg", "audio1/spawn_sound_2.ogg", "audio1/spawn_sound_3.ogg"]

BACKGROUND_IMAGE = "img1/bg.png"