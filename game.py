import pygame
import os

WIDTH = 100*3 + 20*(3+1)
HEIGHT = 100*3 + 20*(3+1)
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Field(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = x
        self.rect.y = y


    def update(self):
        # self.rect.x += 5
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0
        pass

    def new_image (x_img):
        pass


pygame.init()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')


pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player_img = pygame.image.load(os.path.join(img_folder, 'x.png')).convert()
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
fields = pygame.sprite.Group()
for x in range(3):
    for y in range(3):
        field_x = 20*(x+1) + x * 100
        field_y = 20*(y+1) + y * 100
        pos = (x, y)
        f = Field(field_x, field_y, pos)
        fields.add(f)
all_sprites.add(fields)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for field in fields:
                if field.rect.collidepoint(x, y):
                    print(field.pos)

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()