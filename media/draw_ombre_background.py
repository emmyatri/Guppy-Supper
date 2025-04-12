import pygame
import os

def draw_ombre_background(surface, width, height):
    top_color = (255, 200, 120)
    bottom_color = (255, 100, 0)
    for y in range(height):
        blend = y / height
        r = int(top_color[0] * (1 - blend) + bottom_color[0] * blend)
        g = int(top_color[1] * (1 - blend) + bottom_color[1] * blend)
        b = int(top_color[2] * (1 - blend) + bottom_color[2] * blend)
        pygame.draw.line(surface, (r, g, b), (0, y), (width, y))




    }

