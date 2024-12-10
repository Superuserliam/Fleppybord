

# Initialize pygame
pygame.init()

# Game settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PIPE_WIDTH = 60
PIPE_HEIGHT = 500
BIRD_WIDTH = 40
BIRD_HEIGHT = 40
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_GAP = 150
PIPE_VELOCITY = 3
FPS = 60

# Colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen :)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Font
font = pygame.font.SysFont('Arial', 30)

# Game variables
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
pipe_x = SCREEN_WIDTH
pipe_y_top = random.randint(-PIPE_HEIGHT + 100, -50)
pipe_y_bottom = pipe_y_top + PIPE_GAP
score = 0

# Bird class :D
class Bird:
    def __init__(self):
        self.x = 100
        self.y = bird_y
        self.width = BIRD_WIDTH
        self.height = BIRD_HEIGHT

    def move(self):
        self.y += bird_velocity
        bird_velocity += GRAVITY

    def jump(self):
        global bird_velocity
        bird_velocity = JUMP_STRENGTH

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))


# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.top = pipe_y_top
        self.bottom = pipe_y_bottom
        self.width = PIPE_WIDTH

    def move(self):
        self.x -= PIPE_VELOCITY

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.top, self.width, PIPE_HEIGHT))
        pygame.draw.rect(screen, GREEN, (self.x, self.bottom, self.width, SCREEN_HEIGHT - self.bottom))

    def is_offscreen(self):
        return self.x + self.width < 0


# Game loop
def game_loop():
    global pipe_x, bird_y, bird_velocity, pipe_y_top, pipe_y_bottom, score

    bird = Bird()
    pipes = [Pipe(pipe_x)]
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Move and draw bird
        bird.move()
        bird.draw()

        # Move pipes and generate new ones
        for pipe in pipes:
            pipe.move()
            pipe.draw()

        # Remove pipes that are offscreen
        if pipes[0].is_offscreen():
            pipes.pop(0)
            pipes.append(Pipe(SCREEN_WIDTH))

        # Check for collisions with pipes or ground
        for pipe in pipes:
            if (bird.x + bird.width > pipe.x and bird.x < pipe.x + pipe.width and
                (bird.y < pipe.top + PIPE_HEIGHT or bird.y + bird.height > pipe.bottom)):
                running = False  # Game Over

        if bird.y > SCREEN_HEIGHT - bird.height or bird.y < 0:
            running = False  # Game Over

        # Update score
        for pipe in pipes:
            if pipe.x + pipe.width < bird.x and not hasattr(pipe, 'scored'):
                pipe.scored = True
                score += 1

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update display and FPS
        pygame.display.update()
        clock.tick(FPS)


# Start the game
if __name__ == "__main__":
    game_loop()
