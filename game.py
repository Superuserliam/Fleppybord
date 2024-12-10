import pygame
import random
from player import Player
from pipe import Pipe
from utils import draw_text

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PIPE_WIDTH = 60
PIPE_GAP = 150
BIRD_WIDTH = 40
BIRD_HEIGHT = 40

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Set up the clock
clock = pygame.time.Clock()

# Load assets
bg = pygame.image.load('assets/background.png')
bird_img = pygame.image.load('assets/bird.png')
game_over_img = pygame.image.load('assets/game_over.png')
pipe_img = pygame.image.load('assets/pipe.png')

def main():
    bird = Player(bird_img, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
    pipes = []
    score = 0
    ground_y = SCREEN_HEIGHT - 50  # ground height for the game
    
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        # Update game objects
        bird.update()
        if random.random() < 0.02:  # 2% chance of new pipe per frame
            pipes.append(Pipe(PIPE_WIDTH, SCREEN_HEIGHT, PIPE_GAP))
        
        for pipe in pipes:
            pipe.update()
            if pipe.x < -PIPE_WIDTH:
                pipes.remove(pipe)
            if pipe.x + PIPE_WIDTH < bird.x and not pipe.passed:
                pipe.passed = True
                score += 1

        # Check for collisions
        if bird.y + BIRD_HEIGHT >= ground_y or any(pipe.collides_with(bird) for pipe in pipes):
            running = False

        # Draw everything
        screen.blit(bg, (0, 0))  # Background
        for pipe in pipes:
            pipe.draw(screen, pipe_img)
        bird.draw(screen)
        
        # Draw the score
        draw_text(screen, f"Score: {score}", 30, SCREEN_WIDTH // 2, 20)

        pygame.display.flip()

    # Game Over
    screen.fill(BLACK)
    screen.blit(game_over_img, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
    draw_text(screen, f"Final Score: {score}", 40, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()

if __name__ == "__main__":
    main()
