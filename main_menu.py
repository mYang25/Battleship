import pygame

class MainMenuScreen:
    def __init__(self):
        pygame.init()
        self.screen_color = (0, 212, 255)
        
        self.title_font = pygame.font.Font(None, 135)
        self.subtitle_font = pygame.font.Font(None, 52)
        
        self.play_button = pygame.Rect(400, 250, 200, 50)
        self.options_button = pygame.Rect(430, 325, 140, 50)
        self.exit_button = pygame.Rect(430, 390, 140, 50)
        self.button_font = pygame.font.Font(None, 36)
        
        self.play_button_text = self.button_font.render("Play", True, (255, 255, 255))
        self.play_button_text_box = self.play_button_text.get_rect(center=self.play_button.center)
        self.options_button_text = self.button_font.render("Options", True, (255, 255, 255))
        self.options_button_text_box = self.options_button_text.get_rect(center=self.options_button.center)
        self.exit_button_text = self.button_font.render("Exit", True, (255, 255, 255))
        self.exit_button_text_box = self.exit_button_text.get_rect(center=self.exit_button.center)
    
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.collidepoint(event.pos):
                    return "SetupGameScreen"
                if self.options_button.collidepoint(event.pos):
                    return "OptionsScreen"
                if self.exit_button.collidepoint(event.pos):
                    return "Exit"
    
    def update(self):
        pass
    
    def draw(self, surface):
        surface.fill(self.screen_color)
        
        large_text = self.title_font.render("Battleship", True, (0, 0, 0))
        small_text = self.subtitle_font.render("with torpedos, radar, and nukes", True, (0, 0, 0))
        
        surface.blit(large_text, (280, 75))
        surface.blit(small_text, (230, 175))
        
        pygame.draw.rect(surface, (255, 0, 0), self.play_button)
        surface.blit(self.play_button_text, self.play_button_text_box)
        
        pygame.draw.rect(surface, (255, 0, 0), self.options_button)
        surface.blit(self.options_button_text, self.options_button_text_box)
        
        pygame.draw.rect(surface, (255, 0, 0), self.exit_button)
        surface.blit(self.exit_button_text, self.exit_button_text_box)