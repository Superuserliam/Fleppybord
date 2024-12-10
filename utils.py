def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x - text_surface.get_width() // 2, y))
