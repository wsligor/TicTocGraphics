class Settings:
    def __init__(self):
        self.bg_color = (0, 230, 230)
        self.FPS = 60
        self.size = 3

        self.field_side = 100
        self.separator_width = 20

        self.screen_width = self.field_side*self.size + self.separator_width*(self.size+1)
        self.screen_heigth = self.field_side*self.size + self.separator_width*(self.size+1)


        self.state_field = ['empty', 'dagger', 'zero']

        self.empty_color = (0, 0, 0)