import sys
import pygame

from Settings import Settings

def RunGame():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_heigth, setting.screen_width))
    pygame.display.set_caption('Крестики - нолики')

    isFinish = False

    while not isFinish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isFinish = True
        pygame.display.flip()

RunGame()