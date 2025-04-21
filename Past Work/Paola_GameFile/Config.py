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
FOOD_EVENT = pygame.USEREVENT + 1
SCORE=0
#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)


#player settings
##################################
PLAYER_SPEED = 12
PLAYER_IMAGE = pygame.image.load("img_files_go_here/Snake.jpg").convert_alpha()
PLAYER_DEATH_SOUND = pygame.mixer.Sound("audio_files_go_here/Player_death.mp3")

#Food settings
##################################
FOOD_BLIP = {"img_files_go_here/Egg1.jpg","img_files_go_here/Egg2jpg","img_files_go_here/Egg3.jpg"}
FOOD_APPEAR=pygame.mixer.Sound("audio_files_go_here/Food_collection.wav")
FOOD_EATEN=pygame.mixer.Sound("audio_files_go_here/Movement_tick.ogg")

ROCK_OBSTACLE=pygame.image.load("img_files_go_here/Rock.jpg").convert_alpha()
OBS_IMAGE=pygame.image.load("img_files_go_here/Stones.jpg").convert_alpha()

BACKGROUND_IMAGE = pygame.image.load("img_files_go_here/GroundTexture.jpg").convert_alpha()

GAME_OVER_SOUND=pygame.mixer.Sound("audio_files_go_here/Game_over.wav")
LEVEL_UP_SOUND=pygame.mixer.Sound("audio_files_go_here/Success_chime.wav")