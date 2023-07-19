import pygame
from pygame.locals import QUIT

class ScreenManager:
    def __init__(self):
        self.current_screen = None
    
    def set_screen(self, screen):
        self.current_screen = screen
    
    def run(self):
        if self.current_screen is None:
            raise ValueError("No screen is set.")
        
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1000, 500))
        
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    running = False
            
            next_screen = self.current_screen.handle_input(events)
            
            screen.fill((10, 13, 82))
            
            self.current_screen.update()
            
            self.current_screen.draw(screen)
                       
            pygame.display.flip()
            
            clock.tick(60)