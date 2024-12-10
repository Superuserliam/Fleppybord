

class Player:
    def __init__(self, img, x, y):
        self.x = x
        self.y = y
        self.img = img
        self.velocity = 0
        self.gravity = 1
        self.lift = -15

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        if self.y < 0:
            self.y = 0
        elif self.y + self.img.get_height() > 550:  # stop falling after ground level
            self.y = 550 - self.img.get_height()
            self.velocity = 0

    def jump(self):
        self.velocity = self.lift

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
