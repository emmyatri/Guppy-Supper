import pygame
import random
from media import draw_ombre_background, draw_snake, load_sounds, play_background_music

pygame.init()
pygame.mixer.init()

width, height = 640, 480
block_size = 20
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def reset_game():
    return [(100, 100), (80, 100), (60, 100)], (block_size, 0), (300, 300), 0

snake, direction, food, score = reset_game()
speed = 10
is_paused = False
running = True

sounds = load_sounds()
play_background_music()

while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                is_paused = not is_paused
            elif event.key == pygame.K_r:
                snake, direction, food, score = reset_game()

    if is_paused:
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, block_size):
        direction = (0, -block_size)
        sounds["turn"].play()
    elif keys[pygame.K_DOWN] and direction != (0, -block_size):
        direction = (0, block_size)
        sounds["turn"].play()
    elif keys[pygame.K_LEFT] and direction != (block_size, 0):
        direction = (-block_size, 0)
        sounds["turn"].play()
    elif keys[pygame.K_RIGHT] and direction != (-block_size, 0):
        direction = (block_size, 0)
        sounds["turn"].play()

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        sounds["collect"].play()
        while True:
            food = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))
            if food not in snake:
                break
    else:
        snake.pop()

    if (new_head in snake[1:] or
        new_head[0] < 0 or new_head[0] >= width or
        new_head[1] < 0 or new_head[1] >= height):
        sounds["fail"].play()
        pygame.time.wait(1000)
        snake, direction, food, score = reset_game()

    draw_ombre_background(screen, width, height)
    draw_snake(screen, snake, block_size)
    pygame.draw.rect(screen, (255, 255, 255), (*food, block_size, block_size))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
