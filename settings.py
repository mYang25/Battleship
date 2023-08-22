import pygame
import sys

class settings:
    def __init__(self):
        pygame.init()
        
        self.screen_color = (0, 166, 198)
        self.l_blue = (196, 245, 255)
        self.d_blue = (85, 227, 255)
        self.dropdown_color = (128, 128, 128)
        self.text_color = (255, 255, 255)
        
        self.title_font = pygame.font.Font(None, 64)
        
        self.label_font = pygame.font.Font(None, 40)
        self.labels = ["Difficulty", "Torpedoes", "Radar", "Nukes"]
        self.label_positions = [(150, 125), (150, 225), (150, 325), (150, 425)]
        
        self.back_button = pygame.Rect(25, 25, 100, 50)
              
        self.dropdown_menu = pygame.Rect(700, 100, 200, 75)
        self.dropdown_options = ["Easy", "Medium", "Hard", "Not Fair"]
        self.selected_difficulty = None
        self.dropdown_visible = False
               
        self.torpedoes_on_button = pygame.Rect(700, 200, 100, 75)
        self.torpedoes_off_button = pygame.Rect(800, 200, 100, 75)
        self.torpedoes_on = True        
        self.radar_on_button = pygame.Rect(700, 300, 100, 75)
        self.radar_off_button = pygame.Rect(800, 300, 100, 75)
        self.radar_on = True        
        self.nukes_on_button = pygame.Rect(700, 400, 100, 75)
        self.nukes_off_button = pygame.Rect(800, 400, 100, 75)
        self.nukes_on = True
                
        self.clock = pygame.time.Clock()
        
        
        
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.torpedoes_on_button.collidepoint(event.pos):
                    if not self.torpedoes_on:
                        self.torpedoes_on = True
                if self.torpedoes_off_button.collidepoint(event.pos):
                    if self.torpedoes_on:
                        self.torpedoes_on = False
                if self.radar_on_button.collidepoint(event.pos):
                    if not self.radar_on:
                        self.radar_on = True
                if self.radar_off_button.collidepoint(event.pos):
                    if self.radar_on:
                        self.radar_on = False
                if self.nukes_on_button.collidepoint(event.pos):
                    if not self.nukes_on:
                        self.nukes_on = True
                if self.nukes_off_button.collidepoint(event.pos):
                    if self.nukes_on:
                        self.nukes_on = False
                
                if self.dropdown_menu.collidepoint(event.pos):
                    self.dropdown_visible = not self.dropdown_visible
                elif self.dropdown_visible:
                    for i, option in enumerate(self.dropdown_options):
                        option_rect = pygame.Rect(self.dropdown_menu.left, self.dropdown_menu.bottom + i * 25, self.dropdown_menu.width, 25)
                        if option.rect.collidepoint(event.pos):
                            self.selected_option = option
                            self.dropdown_visible = False
                        
                        
                        
    def update(self):
        pygame.display.flip()
    
    
    
    def draw(self, surface):
        surface.fill(self.screen_color)
        
        pygame.draw.rect(surface, self.d_blue, self.torpedoes_on_button)
        pygame.draw.rect(surface, self.l_blue, self.torpedoes_off_button)
        pygame.draw.rect(surface, self.d_blue, self.radar_on_button)
        pygame.draw.rect(surface, self.l_blue, self.radar_off_button)
        pygame.draw.rect(surface, self.d_blue, self.nukes_on_button)
        pygame.draw.rect(surface, self.l_blue, self.nukes_off_button)
        
        
        
        for label, position in zip(self.labels, self.label_positions):
            text_surface = self.label_font.render(label, True, self.text_color)
            text_rect = text_surface.get_rect()
            text_rect.topleft = position
            surface.blit(text_surface, text_rect)
            
        title_surface = self.title_font.render("Settings", True, self.text_color)
        title_rect = title_surface.get_rect()
        title_rect.topleft = (400, 30)
        surface.blit(title_surface, title_rect)
        
        pygame.draw.rect(surface, (150, 150, 150), self.back_button)
        back_button_text_surface = self.label_font.render("Back", True, (0, 0, 0))
        back_button_text_rect = back_button_text_surface.get_rect(center=self.back_button.center)
        surface.blit(back_button_text_surface, back_button_text_rect)    