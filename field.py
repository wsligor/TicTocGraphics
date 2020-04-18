import pygame
from pygame.sprite import Sprite
import settings as s

class Field(Sprite):
    def __init__(self, screen, setting: s.Settings, x, y):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.state = -1
        self.rect =pygame.Rect(x, y, setting.field_side, setting.field_side)
        self.color = (255, 255, 255)
        pass

    def get_state(self):
        return self.state

    def set_state(self, state):
        if self.state == -1:
            self.state = state

    def draw_field(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

