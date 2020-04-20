import settings as s
import pygame
from field import Field

class Game_Function:
    def __init__(self, screen, setting: s.Settings):
        self.screen = screen
        self.setting = setting
        self.data = [[-1, -1, -1],[-1, -1, -1], [-1, -1, -1]]
        pass

    def create_fields(self, fields):
        for x in range(self.setting.size):
            for y in range(self.setting.size):
                field_x = self.setting.separator_width + x*self.setting.field_side
                field_y = self.setting.separator_width + y*self.setting.field_side
                rect = Field(self.screen, self.setting, field_x, field_y)
                self.data[x] [y] = rect
                fields.add(rect)

    def update_screen(self, screen, setting, fields):
        for field in fields.sprites():
            field.draw_field()
        pygame.display.flip()
        pass
