import pygame
from main_menu import MainMenuScreen
from game_screen import GameScreen
from screen_manager import ScreenManager
from settings import settings


if __name__ == "__main__":
    screen_manager = ScreenManager()
    game_screen = GameScreen()
    main_menu_screen = MainMenuScreen()
    settings_screen = settings()
    
    screen_manager.set_screen(settings_screen)
    screen_manager.run()