

class Pipe:
    def __init__(self, width, screen_height, gap):
        self.x = screen_width
        self.width = width
        self.height = random.randint(100, screen_height - gap - 100)
        self.gap = gap
        self.passed = False
    
    def update(self):
        self.x -= 5

    def draw(self, screen, pipe_img):
        top_rect = pygame.Rect(self.x, 0, self.width, self.height)
        bottom_rect = pygame.Rect(self.x, self.height + self.gap, self.width, screen_height - self.height - self.gap)
        screen.blit(pipe_img, (self.x, 0), top_rect)  # top pipe
        screen.blit(pipe_img, (self.x, self.height + self.gap), bottom_rect)  # bottom pipe
    
    def collides_with(self, player):
        pipe_rect_top = pygame.Rect(self.x, 0, self.width, self.height)
        pipe_rect_bottom = pygame.Rect(self.x, self.height + self.gap, self.width, 600 - self.height - self.gap)
        bird_rect = pygame.Rect(player.x, player.y, 40, 40)
        
        return pipe_rect_top.colliderect(bird_rect) or pipe_rect_bottom.colliderect(bird_rect)
