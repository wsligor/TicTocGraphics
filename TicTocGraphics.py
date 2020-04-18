import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_function import Game_Function


def RunGame():
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_heigth, setting.screen_width))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Крестики - нолики')

    isFinish = False

    gf = Game_Function(screen, setting)

    fields = Group()

    gf.create_fields()

    while not isFinish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isFinish = True
        screen.fill(setting.bg_color)
        gf.update_screen(screen, setting, fields)


    pygame.quit()
    sys.exit()

RunGame()