import pygame
def draw_snake(surface, body, size):
    TEAL = (0, 128, 128)
    for segment in body:
            pygame.draw.rect(surface, TEAL, (*segment, size, size))