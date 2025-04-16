import pygame, sys, random
from Config import *
from Food import FOOD
from Player import Player
from ObstacleElements import OBSTACLE

#main game loop
def main():

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption("Snake Merge") #This function changes the name of the game in the window

    pygame.time.set_timer(FOOD_EVENT, 1000) #time in milliseconds

    clock = pygame.time.Clock()

    #GAME OVER SCREEN
    font = pygame.font.Font(None, 48)
    game_over = font.render("GAME OVER!", True, BLACK)
    game_over_rect = game_over.get_rect(center=(WIDTH//2, HEIGHT//2))
    game_over_screen = pygame. Surface((WIDTH, HEIGHT))
    game_over_screen.set_alpha(100)
    game_over_screen.fill(YELLOW)

    #load background image from files
    background = pygame.image.load(BACKGROUND_IMAGE)

    #create dictionary for Food
    food_list = []
    obstacle_list = []
    #initialize player file
    player = Player()

    #bool for running game loop
    running = True

    while running:

        #initialize key strokes
        keys = pygame.key.get_pressed()

        #quit game with either exit or ESC key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

            #initialize meteor event
            if event.type == FOOD_EVENT:

                food = FOOD()
                food_list.append(food)
                food.spawn_sound.play()

                pygame.time.set_timer(FOOD_EVENT, random.randint(800, 1500))

        #create opening screen with background
        screen.blit(background, (0,0))

        #Obstacle logic and movements
        for obstacle in obstacle_list[:]:
            obstacle.fall()
            obstacle.draw(screen)

            #handling the event of character death
            if player.alive and player.rect.colliderect(obstacle.rect):
                player.deadSound.play()
                player.alive = False
        if random.random() < 0.01:
            new_obstacle = OBSTACLE(OBS_IMAGE,pygame.time.get_ticks())
            obstacle_list.append(new_obstacle)
            new_obstacle.spawn_sound.play()

        #calling movement and image from payer file
        if player.alive:
            player.move()
            player.draw()
        else:
            screen.blit(game_over_screen, (0,0))
            screen.blit(game_over, game_over_rect)
            pygame.mixer.Sound(GAME_OVER_SOUND).play()

        pygame.display.flip()
        clock.tick(FPS) #pulling FPS from Config file

    pygame.quit()

if __name__ == "__main__":
    main()