import pygame
import random
import sys
import time

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Fonts
FONT = pygame.font.SysFont("arial", 36)
SMALL_FONT = pygame.font.SysFont("arial", 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
player_score = 0
computer_score = 0
max_score = 5
choices = ["rock", "paper", "scissors"]
round_winner = ""
timer = 5  # seconds to choose
player_choice = None
computer_choice = None
clock = pygame.time.Clock()

# Button setup
def draw_button(text, x, y, w, h):
    pygame.draw.rect(WIN, BLACK, (x, y, w, h), 2)
    label = FONT.render(text, True, BLACK)
    WIN.blit(label, (x + w//2 - label.get_width()//2, y + h//2 - label.get_height()//2))
    return pygame.Rect(x, y, w, h)

def determine_winner(p_choice, c_choice):
    if p_choice == c_choice:
        return "tie"
    if (p_choice == "rock" and c_choice == "scissors") or \
       (p_choice == "paper" and c_choice == "rock") or \
       (p_choice == "scissors" and c_choice == "paper"):
        return "player"
    return "computer"

# Main game loop
def main():
    global player_score, computer_score, round_winner, timer, player_choice, computer_choice

    running = True
    round_start_time = time.time()

    while running:
        WIN.fill(WHITE)

        # Timer countdown
        time_left = max(0, int(timer - (time.time() - round_start_time)))
        timer_text = FONT.render(f"Time Left: {time_left}s", True, BLACK)
        WIN.blit(timer_text, (WIDTH//2 - timer_text.get_width()//2, 20))

        # Score display
        score_text = FONT.render(f"You: {player_score}  |  Computer: {computer_score}", True, BLACK)
        WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 80))

        # Show last choices
        if player_choice:
            player_text = SMALL_FONT.render(f"You chose: {player_choice}", True, BLACK)
            WIN.blit(player_text, (50, HEIGHT - 100))
        if computer_choice:
            computer_text = SMALL_FONT.render(f"Computer chose: {computer_choice}", True, BLACK)
            WIN.blit(computer_text, (WIDTH - 250, HEIGHT - 100))

        # Result message
        if round_winner:
            result_text = FONT.render(round_winner, True, BLACK)
            WIN.blit(result_text, (WIDTH//2 - result_text.get_width()//2, 140))

        # Draw buttons
        rock_btn = draw_button("Rock", 100, 200, 150, 80)
        paper_btn = draw_button("Paper", 325, 200, 150, 80)
        scissors_btn = draw_button("Scissors", 550, 200, 150, 80)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN and time_left > 0:
                if rock_btn.collidepoint(event.pos):
                    player_choice = "rock"
                elif paper_btn.collidepoint(event.pos):
                    player_choice = "paper"
                elif scissors_btn.collidepoint(event.pos):
                    player_choice = "scissors"
                else:
                    continue

                computer_choice = random.choice(choices)
                winner = determine_winner(player_choice, computer_choice)

                if winner == "player":
                    player_score += 1
                    round_winner = "You won the round!"
                elif winner == "computer":
                    computer_score += 1
                    round_winner = "Computer won the round!"
                else:
                    round_winner = "It's a tie!"

                round_start_time = time.time()
                player_choice = None
                computer_choice = None

        # If time runs out
        if time_left == 0 and player_choice is None:
            round_winner = "Time's up! Computer wins this round."
            computer_score += 1
            round_start_time = time.time()

        # Check win condition
        if player_score >= max_score and computer_score >= max_score:
            round_winner = "It's a tie game!"
            running = False
        elif player_score >= max_score:
            round_winner = "You win the game!"
            running = False
        elif computer_score >= max_score:
            round_winner = "Computer wins the game!"
            running = False

        clock.tick(30)

    # Game over screen
    WIN.fill(WHITE)
    end_text = FONT.render(round_winner, True, BLACK)
    WIN.blit(end_text, (WIDTH//2 - end_text.get_width()//2, HEIGHT//2 - 50))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

main()
