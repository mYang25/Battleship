import pygame
import sys

class options:
    def __init__(self):
        pygame.init()
        
        self.screen_color = (0, 212, 255)
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
                
                if self.dropdown_button.collidepoint(event.pos):
                    self.dropdown_visible = not self.dropdown_visible
                elif self.dropdown_visible:
                    for i, option in enumerate(self.dropdown_options):
                        option_rect = pygame.Rect(self.dropdown_menu.left, self.dropdown_menu.bottom + i * 25, self.dropdown_menu.width, 25)
                        if option.rect.collidepoint(event.pos):
                            self.selected_option = option
                            self.dropdown_visible = False
                        
                        
                        
    def update(self):
        pass
    
    def draw(self, surface):
        surface.fill(self.screen_color)
        
        
        
        
    

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_button(x, y, text, highlighted=False):
    button_color = WHITE if not highlighted else GRAY
    pygame.draw.rect(screen, button_color, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
    draw_text(text, x + 10, y + 10, BLACK)

def draw_switch(x, y, text, is_on=False):
    switch_color = (0, 255, 0) if is_on else (255, 0, 0)
    pygame.draw.rect(screen, switch_color, (x, y, SWITCH_WIDTH, SWITCH_HEIGHT))
    draw_text(text, x + 100, y + 10, BLACK)

def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check for button clicks
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if BUTTON_SPACING <= mouse_y <= BUTTON_SPACING + BUTTON_HEIGHT:
                    if 50 <= mouse_x <= 50 + BUTTON_WIDTH:
                        selected_button = "easy"
                    elif 300 <= mouse_x <= 300 + BUTTON_WIDTH:
                        selected_button = "medium"
                    elif 550 <= mouse_x <= 550 + BUTTON_WIDTH:
                        selected_button = "hard"
                else:
                    selected_button = None

        # Draw the options screen
        screen.fill(WHITE)

        # Draw buttons
        draw_button(50, BUTTON_SPACING, "Easy", selected_button == "easy")
        draw_button(300, BUTTON_SPACING, "Medium", selected_button == "medium")
        draw_button(550, BUTTON_SPACING, "Hard", selected_button == "hard")

        # Draw switches
        draw_switch(100, SWITCH_SPACING, "Torpedoes", torpedoes_on)
        draw_switch(300, SWITCH_SPACING, "Radar", radar_on)
        draw_switch(500, SWITCH_SPACING, "Nukes", nukes_on)

        # Draw "Back" button
        draw_button(350, HEIGHT - 100, "Back")

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()