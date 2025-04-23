import pygame, sys, random
from Config import *
from Worm import Worm
from PlayerFile import Player
from Bubble import Bubble
def draw_text(screen, text, size, x, y, color):
    font = pygame.font.SysFont("segoeprint", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_button(screen, text, size, x, y, color, hover_color, mouse_pos):
    font = pygame.font.SysFont("segoeprint", size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)

    # Create button rectangle
    button_rect = pygame.Rect(text_rect.x - 20, text_rect.y - 10,
                            text_rect.width + 40, text_rect.height + 20)

    # Check if mouse is hovering over button
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, button_rect, border_radius=10)
    else:
        pygame.draw.rect(screen, color, button_rect, border_radius=10)

    screen.blit(text_surface, text_rect)
    return button_rect

def show_menu(screen, background):
    menu_running = True
    clock = pygame.time.Clock()

    while menu_running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(mouse_pos):
                    return True  # Start the game

        # Draw menu
        icon = pygame.image.load(PLAYER_IMAGE)
        screen.blit(background, (0,0))
        screen.blit(icon, (WIDTH/2.2, HEIGHT - 700))

        # Draw title
        draw_text(screen, "Guppy Supper", 64, WIDTH//2, HEIGHT//3, WHITE)

        # Draw instructions
        instructions = [
            "Help the fish eat as many worms as possible!",
            "Use arrow keys or WASD to move",
            "Small worms = 3 point",
            "Medium worms = 2 points",
            "Large worms = 1 points",
            "Avoid the bubbles!",
            "Press ESC to quit"
        ]

        for i, line in enumerate(instructions):
            draw_text(screen, line, 20, WIDTH//2, HEIGHT//2 - 40 + i * 30, WHITE)

        # Draw start button
        start_button = draw_button(screen, "Start Game", 36, WIDTH//2, HEIGHT - 100,
                                 (100, 200, 100), (150, 250, 150), mouse_pos)

        pygame.display.flip()
        clock.tick(60)
#main game loop
def main():

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Guppy Supper")#changes the name of the game in the window


    font = pygame.font.SysFont("segoeprint", 36)
    score = 0


    pygame.time.set_timer(WORM_EVENT, 1000)
    pygame.time.set_timer(BUBBLE_EVENT, 2000)


    clock = pygame.time.Clock()

    #GAME OVER SCREEN


    def draw_score_box():
        score_box = font.render(f" Worms eaten: {score} ", True, BLACK)
        background_rect = score_box.get_rect()
        background_rect.center = (WIDTH/2, 35)
        s = pygame.Surface((background_rect.width-5, background_rect.height-5))
        s.set_alpha(1500)
        s.fill(WHITE)
        screen.blit(s, background_rect)


    # Draw score text
        screen.blit(score_box, (background_rect.x, background_rect.y))

    game_over = font.render(f"You Lost!", True, WHITE)
    game_over_rect = game_over.get_rect(center=(WIDTH//2, HEIGHT/2.2))
    game_over_screen = pygame. Surface((WIDTH, HEIGHT))
    game_over_screen.set_alpha(100)
    game_over_screen.fill(BLACK)


    # load background image from files
    background = pygame.image.load(BACKGROUND_IMAGE)
    background2 = pygame.image.load(EXTRA_BG)

    if not show_menu(screen, background):
        return


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
                bubble.spawn_sound.play()
                pygame.time.set_timer(WORM_EVENT, random.randint(800, 1500))


        #create opening screen with background
        screen.blit(background, (0,0))
        screen.blit(background2, (0, 0))



        #meteor logic and movements
        for worm in worms[:]:
            worm.fall()
            worm.draw(screen)

            if worm.rect.colliderect(player.rect):
                if worm.types == "small":
                    score += 3
                if worm.types == "medium":
                    score += 2
                if worm.types == 'big':
                    score += 1
                if worm.types == "rare":
                    score += 5
                worms.remove(worm)

        for bubble in bubbles[:]:
            bubble.rise()
            bubble.draw(screen)

            if player.alive and bubble.rect.colliderect(player.rect):
                player.alive = False
                bubbles.remove(bubble)
                player.deadSound.play()
                pygame.time.set_timer(WORM_EVENT, 0)
                pygame.time.set_timer(BUBBLE_EVENT, 0)
                final_score = font.render(f"Final Score: {score}", True, WHITE)
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