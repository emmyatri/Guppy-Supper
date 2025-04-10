import pygame, sys, random
from Config import *
from Meteor import Meteor
from Player import Player

#main game loop
def main():

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Meteor Dodge") #This function changes the name of the game in the window

    pygame.time.set_timer(METEOR_EVENT, 1000) #time in milliseconds

    clock = pygame.time.Clock()

    #GAME OVER SCREEN
    font = pygame.font.Font(None, 48)
    game_over = font.render("You Lost!", True, WHITE)
    game_over_rect = game_over.get_rect(center=(WIDTH//2, HEIGHT//2))
    game_over_screen = pygame. Surface((WIDTH, HEIGHT))
    game_over_screen.set_alpha(100)
    game_over_screen.fill(BLACK)

    #load background image from files
    background = pygame.image.load(BACKGROUND_IMAGE).convert()

    #create dictionary for Meteors
    meteors = []
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
            if event.type == METEOR_EVENT:

                meteor = Meteor()
                meteors.append(meteor)
                meteor.spawn_sound.play()

                pygame.time.set_timer(METEOR_EVENT, random.randint(800, 1500))

        #create opening screen with background
        screen.blit(background, (0,0))

        #meteor logic and movements
        for meteor in meteors[:]:
            meteor.fall()
            meteor.draw(screen)

            if meteor.rect.top > HEIGHT:
                meteors.remove(meteor)

            #handling the event of character death
            if player.alive and meteor.rect.colliderect(player.rect):
                player.deadSound.play()
                player.alive = False

        #calling movement and image from payer file
        if player.alive:
            player.move()
            player.draw()
        else:
            screen.blit(game_over_screen, (0,0))
            screen.blit(game_over, game_over_rect)

        pygame.display.flip()
        clock.tick(FPS) #pulling FPS from Config file

    pygame.quit()

if __name__ == "__main__":
    main()