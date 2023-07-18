import pygame

class MainMenuScreen:
    def __init__(self):
        self.button_play_rect = pygame.Rect(100, 200, 200, 50)
    
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_play_rect.collidepoint(event.pos):
                    return "SetupGameScreen"
    
    def update(self):
        pass
    
    def draw(self, surface):
        # Draw the "Play" button
        pygame.draw.rect(surface, (255, 0, 0), self.button_play_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Play", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.button_play_rect.center)
        surface.blit(text, text_rect)
        
