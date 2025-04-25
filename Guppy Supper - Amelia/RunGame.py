import pygame, sys, random
from Config import *
from PlayerFile import Player
from Bubble import Bubble
from Worm import Worm
from RareWorm import RareWorm
from Shark import Shark

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
            if event.type == pygame.K_RETURN:
                return True

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
            "Rare worms = 5 points",
            "Avoid the bubbles and sharks!",
            "Press ESC to quit"
        ]

        for i, line in enumerate(instructions):
            draw_text(screen, line, 20, WIDTH//2, HEIGHT//2 - 40 + i * 30, WHITE)

        # Draw start button
        start_button = draw_button(screen, "Start Game", 36, WIDTH//2, HEIGHT - 100,
                                 (100, 200, 100), (150, 250, 150), mouse_pos)

        pygame.display.flip()
        clock.tick(60)

def show_game_over(screen, background, final_score):
    game_over_running = True
    clock = pygame.time.Clock()

    while game_over_running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(mouse_pos):
                    return "restart"
                if quit_button.collidepoint(mouse_pos):
                    return "quit"

        # Draw game over screen
        screen.blit(background, (0,0))

        # Draw "Game Over" text
        draw_text(screen, "Game Over!", 64, WIDTH//2, HEIGHT//3, WHITE)
        draw_text(screen, f"Final Score: {final_score}", 48, WIDTH//2, HEIGHT//2, WHITE)

        # Draw buttons
        restart_button = draw_button(screen, "Play Again", 36, WIDTH//2, HEIGHT - 200,
                                   (100, 200, 100), (150, 250, 150), mouse_pos)
        quit_button = draw_button(screen, "Quit Game", 36, WIDTH//2, HEIGHT - 100,
                                (200, 100, 100), (250, 150, 150), mouse_pos)

        pygame.display.flip()
        clock.tick(60)

#main game loop
def main():

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("audio_files_go_here/wave1.flac")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Guppy Supper")#changes the name of the game in the window
    font = pygame.font.SysFont("segoeprint", 36)
    clock = pygame.time.Clock()

    #SCORE


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



    # load background image from files
    background = pygame.image.load(BACKGROUND_IMAGE)
    background2 = pygame.image.load(EXTRA_BG)

    #bool for running game loop
    running = True

    while running:

        if not show_menu(screen, background):
            break

        score = 0
        worms = []
        bubbles = []
        sharks = []
        # initialize player file
        player = Player()
        rare_worm = RareWorm()

        pygame.time.set_timer(WORM_EVENT, 1000)
        pygame.time.set_timer(BUBBLE_EVENT, 2000)
        pygame.time.set_timer(RARE_WORM_EVENT, 10000)
        pygame.time.set_timer(SHARK_EVENT, 1000)

        game_running = True

        #initialize key strokes
        while game_running:

            keys = pygame.key.get_pressed()

            # quit game with either exit or ESC key
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if keys[pygame.K_ESCAPE]:
                    sys.exit(0)

                # initialize event
                if event.type == WORM_EVENT:
                    worm = Worm()
                    worms.append(worm)
                    worm.spawn_sound.play()

                    pygame.time.set_timer(WORM_EVENT, random.randint(800, 1500))

                if event.type == RARE_WORM_EVENT:
                    rare_worm = RareWorm()
                    worms.append(rare_worm)
                    worm.spawn_sound.play()

                    pygame.time.set_timer(RARE_WORM_EVENT, random.randint(2000, 6000))

                if event.type == BUBBLE_EVENT:
                    bubble = Bubble()
                    bubbles.append(bubble)
                    bubble.spawn_sound.play()
                    pygame.time.set_timer(WORM_EVENT, random.randint(800, 1500))

                if event.type == SHARK_EVENT:  # 20% chance to spawn a shark
                    if random.random() <= 0.2:  # used random.random to make the shark spawn at 0.2
                        shark = Shark()
                        sharks.append(shark)
                        shark.spawn_sound.play()
                    pygame.time.set_timer(SHARK_EVENT, random.randint(1000, 5000))  # 20% chance to spawn a shark
            if not game_running:
                break
            # create opening screen with background
            screen.blit(background, (0, 0))
            screen.blit(background2, (0, 0))

            # worm logic and movements
            for worm in worms[:]:
                worm.fall()
                worm.draw(screen)

                if worm.rect.top > HEIGHT:
                    worms.remove(worm)
                    continue

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
                    pygame.mixer.music.load("audio_files_go_here/Rise01.aif")
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.play(1)

            for bubble in bubbles[:]:
                bubble.rise()
                bubble.draw(screen)

                if bubble.rect.bottom < 0:
                    bubbles.remove(bubble)
                    continue

                if player.alive and bubble.rect.colliderect(player.rect):
                    player.alive = False
                    bubbles.remove(bubble)
                    player.deadSound.play()
                    pygame.time.set_timer(WORM_EVENT, 0)
                    pygame.time.set_timer(BUBBLE_EVENT, 0)
                    pygame.time.set_timer(RARE_WORM_EVENT, 0)
                    final_score = font.render(f"Final Score: {score}", True, WHITE)
                    final_score_rect = final_score.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    final_score_screen = pygame.Surface((WIDTH, HEIGHT))
                    final_score_screen.set_alpha(100)
                    final_score_screen.fill(BLACK)

            for shark in sharks[:]:
                shark.move()
                shark.draw(screen)
                is_alive = shark.draw(screen)
                if not is_alive:
                    sharks.remove(shark)

                collision_rect = shark.rect.inflate(-400, -400)
                if player.rect.colliderect(collision_rect):
                    player.alive = False
                    sharks.remove(shark)
                    player.deadSound.play()
                    pygame.time.set_timer(WORM_EVENT, 0)
                    pygame.time.set_timer(BUBBLE_EVENT, 0)
                    pygame.time.set_timer(RARE_WORM_EVENT, 0)
                    pygame.time.set_timer(SHARK_EVENT, 0)
                    final_score = font.render(f"Final Score: {score}", True, WHITE)
                    final_score_rect = final_score.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    final_score_screen = pygame.Surface((WIDTH, HEIGHT))
                    final_score_screen.set_alpha(100)
                    final_score_screen.fill(BLACK)

            # calling movement and image from payer file
            if player.alive:
                player.move()
                player.draw()
                draw_score_box()
            else:
                pygame.time.set_timer(WORM_EVENT, 0)
                pygame.time.set_timer(BUBBLE_EVENT, 0)
                pygame.time.set_timer(RARE_WORM_EVENT, 0)
                pygame.time.set_timer(SHARK_EVENT, 0)
                pygame.mixer.music.stop()

                # Show game over screen
                result = show_game_over(screen, background, score)
                if result == "quit":
                    running = False
                    break
                elif result == "restart":
                    game_running = False
                    break

            pygame.display.flip()
            clock.tick(FPS)  # pulling FPS from Config file





if __name__ == "__main__":
    main()
