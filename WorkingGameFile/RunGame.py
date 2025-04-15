import pygame, sys, random
from Config import *
from Worm import Worm
from PlayerFile import Player
from Bubble import Bubble

#main game loop
def main():

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Guppy Supper") #This function changes the name of the game in the window

    pygame.time.set_timer(WORM_EVENT, 1000)
    pygame.time.set_timer(BUBBLE_EVENT, 2000)#time in milliseconds

    clock = pygame.time.Clock()

    #GAME OVER SCREEN
    font = pygame.font.Font(None, 48)
    score = 0

    def draw_score_box():
        score_box = font.render(f"Worms eaten: {score}", True, WHITE)
        background_rect = score_box.get_rect()
        background_rect.bottomleft = (20,HEIGHT-20)
        s = pygame.Surface((background_rect.width, background_rect.height))
        s.set_alpha(128)
        s.fill(BLACK)
        screen.blit(s, background_rect)


    # Draw score text
        screen.blit(score_box, (background_rect.x, background_rect.y))

    game_over = font.render(f"You Lost!", True, WHITE)
    game_over_rect = game_over.get_rect(center=(WIDTH//2, HEIGHT//3))
    game_over_screen = pygame. Surface((WIDTH, HEIGHT))
    game_over_screen.set_alpha(100)
    game_over_screen.fill(BLACK)


    # load background image from files
    background = pygame.image.load(BACKGROUND_IMAGE)



    #create dictionary for Meteors
    worms = []
    bubbles = []
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
            if event.type == WORM_EVENT:

                worm = Worm()
                worms.append(worm)
                worm.spawn_sound.play()

                pygame.time.set_timer(WORM_EVENT, random.randint(800, 1500))

            if event.type == BUBBLE_EVENT:

                bubble = Bubble()
                bubbles.append(bubble)
                pygame.time.set_timer(WORM_EVENT, random.randint(800, 1500))


        #create opening screen with background
        screen.blit(background, (0,0))



        #meteor logic and movements
        for worm in worms[:]:
            worm.fall()
            worm.draw(screen)

            if worm.rect.colliderect(player.rect):
                worms.remove(worm)
                score += 1

        for bubble in bubbles[:]:
            bubble.rise()
            bubble.draw(screen)

            if bubble.rect.colliderect(player.rect):
                player.alive = False
                final_score = font.render(f"Final Score {score}", True, WHITE)
                final_score_rect = final_score.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                final_score_screen = pygame.Surface((WIDTH, HEIGHT))
                final_score_screen.set_alpha(100)
                final_score_screen.fill(BLACK)





        #calling movement and image from payer file
        if player.alive:
            player.move()
            player.draw()
            draw_score_box()

        else:
            screen.blit(game_over_screen, (0,0))
            screen.blit(game_over, game_over_rect)
            screen.blit(final_score, final_score_rect)



        pygame.display.flip()
        clock.tick(FPS) #pulling FPS from Config file

    pygame.quit()

if __name__ == "__main__":
    main()