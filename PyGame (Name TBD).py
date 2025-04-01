import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (500,500)
screen = pygame.display.set_mode(resolution)

pygame.display.set_caption("Game Name TBD")

pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

while True:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    screen.fill(color=(0,0,0))

    pygame.display.flip()

    clock.tick(60)