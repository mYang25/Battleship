import pygame
from main_menu import MainMenuScreen
from game_screen import GameScreen
from screen_manager import ScreenManager
from options import Options


if __name__ == "__main__":
    screen_manager = ScreenManager()
    game_screen = GameScreen()
    main_menu_screen = MainMenuScreen()
    options_screen = Options()
    
    screen_manager.set_screen(options_screen)
    screen_manager.run()