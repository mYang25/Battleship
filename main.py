import pygame
from main_menu import MainMenuScreen
from game_screen import GameScreen
from screen_manager import ScreenManager


if __name__ == "__main__":
    screen_manager = ScreenManager()
    game_screen = GameScreen()
    main_menu_screen = MainMenuScreen()
    
    screen_manager.set_screen(main_menu_screen)
    screen_manager.run()