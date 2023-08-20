import pygame
import sys

class Options:
    def __init__(self):
        pygame.init()
        
        self.screen_color = (0, 166, 198)
        self.l_blue = (196, 245, 255)
        self.d_blue = (85, 227, 255)
        self.dropdown_color = (128, 128, 128)
        
        self.font = pygame.font.Font(None, 40)
        
        self.dropdown_menu = pygame.Rect(700, 200, 200, 25)
        self.torpedoes_on_button = pygame.Rect(700, 250, 50, 25)
        self.torpedoes_off_button = pygame.Rect(800, 250, 50, 25)
        self.radar_on_button = pygame.Rect(700, 300, 50, 25)
        self.radar_off_button = pygame.Rect(800, 300, 50, 25)
        self.nukes_on_button = pygame.Rect(700, 350, 50, 25)
        self.nukes_off_button = pygame.Rect(800, 350, 50, 25)
        
        self.clock = pygame.time.Clock()
        self.labels = ["Difficulty", "Torpedoes", "Radar", "Nukes"]
        self.label_positions = [(50, 100), (50, 200), (50, 300), (50, 400)]
        self.dropdown_options = ["Easy", "Medium", "Hard", "Not Fair"]
        self.selected_difficulty = None
        self.dropdown_visible = False
        self.torpedoes_on = True
        self.radar_on = True
        self.nukes_on = True
        
        
        
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.torpedoes_on_button.collidepoint(event.pos):
                    if not self.torpedoes_on:
                        self.torpedoes_on = True
                        self.torpedoes_on_button.fill(self.d_blue)
                        self.torpedoes_off_button.fill(self.l_blue)
                if self.torpedoes_off_button.collidepoint(event.pos):
                    if self.torpedoes_on:
                        self.torpedoes_on = False
                        self.torpedoes_off_button.fill(self.d_blue)
                        self.torpedoes_on_button.fill(self.l_blue)
                if self.radar_on_button.collidepoint(event.pos):
                    if not self.radar_on:
                        self.radar_on = True
                        self.radar_on_button.fill(self.d_blue)
                        self.radar_off_button.fill(self.l_blue)
                if self.radar_off_button.collidepoint(event.pos):
                    if self.radar_on:
                        self.radar_on = False
                        self.radar_off_button.fill(self.d_blue)
                        self.radar_on_button.fill(self.l_blue)
                if self.nukes_on_button.collidepoint(event.pos):
                    if not self.nukes_on:
                        self.nukes_on = True
                        self.nukes_on_button.fill(self.d_blue)
                        self.nukes_off_button.fill(self.l_blue)
                if self.nukes_off_button.collidepoint(event.pos):
                    if self.nukes_on:
                        self.nukes_on = False
                        self.nukes_off_button.fill(self.d_blue)
                        self.nukes_on_button.fill(self.l_blue)
                
                if self.dropdown_button.collidepoint(event.pos):
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
        
        
        
        