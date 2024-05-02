import pygame
import sys
from screens.main_menu import MainMenu

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Final Dashboard")

font = 'font/Pixeltype.ttf'

def main():
    current_screen = MainMenu(font)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            new_screen = current_screen.handle_event(event)
            if new_screen:
                current_screen = new_screen

        current_screen.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
