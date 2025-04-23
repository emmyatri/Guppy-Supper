import pygame, sys
pygame.init()
pygame.mixer.init()

#general settings
##################################
WIDTH, HEIGHT = 800,800
RESOLUTION = (WIDTH, HEIGHT)
FPS = 60
SCREEN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_mode(RESOLUTION)

CLOCK = pygame.time.Clock()
CLOCK.tick(60)

#custom meteor event
WORM_EVENT = pygame.USEREVENT + 1
BUBBLE_EVENT = pygame.USEREVENT + 2
RARE_WORM_EVENT = pygame.USEREVENT + 3
SHARK_EVENT = pygame.USEREVENT + 4

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

#player settings
##################################
PLAYER_SPEED = 12
PLAYER_IMAGE = "img_files_go_here/fish_sprite.png"
PLAYER_DEATH_SOUND = "audio_files_go_here/pop1.ogg"

#meteor settings
##################################
WORM_SPEED = {
    "big" : 8,
    "medium" : 9,
    "small" : 10
}

RARE_WORM_SPEED = {"rare" : 6}

BUBBLE_SPEED = {
    "big" : 8,
    "medium" : 10,
    "small" : 10,
}


# Creative assets for player/meteor/background
##################################

WORM_PATHS = {
    "big" : ["img_files_go_here/worm1.png", "img_files_go_here/worm2.png", "img_files_go_here/worm3.png"],
    "medium" : ["img_files_go_here/medworm1.png", "img_files_go_here/medworm2.png", "img_files_go_here/medworm3.png" ],
    "small" : ["img_files_go_here/smallworm1.png", "img_files_go_here/smallworm2.png", "img_files_go_here/smallworm3.png"]
}

RARE_WORM_PATH = {"rare" : ["img_files_go_here/GoldenWorm_80x80.png"]}

SHARK_PATHS = "img_files_go_here/Shark.png"
SHARK_SOUND = "audio_files_go_here/SharkThemeSong.ogg"

BUBBLE_PATHS = {
    "big" : ["img_files_go_here/bigbubble1.png",],
    "medium" : ["img_files_go_here/bubble1.png",],
    "small" : ["img_files_go_here/bubble1.png"]
}

SOUNDS = ["audio_files_go_here/SoundJump1.wav"]
BUBBLE_SOUNDS = ["audio_files_go_here/bubbles-single2.wav", "audio_files_go_here/bubbles-single1.wav", "audio_files_go_here/bubbles-single3.wav"]


GAME_MUSIC = ["audio_files_go_here/Seagull Big Ambient.wav"]

BACKGROUND_IMAGE = "img_files_go_here/background.png"
EXTRA_BG = "img_files_go_here/background2.png"
GRADIENT = "img_files_go_here/gradient.png"

