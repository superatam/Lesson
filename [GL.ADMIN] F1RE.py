import pygame
import os


pygame.init()

game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "image_TANK228")
player_image = pygame.image.load(os.path.join(image_folder, "tilled.png")).convert()

screen_color = (0, 0, 0)  # color background
all_sprites = pygame.sprite.Group()
fps = 120

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((160, 220))
        self.image.fill((200, 159, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

    def update(self):
        self.rect.x += 4
        if self.rect.left > width:
           self.rect.right = 0


pygame.mixer.init()  # Sound initialization
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("dino")  # name
clock = pygame.time.Clock()  # FPS
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
run = True

while run:
    # x
    clock.tick(fps)

    for event in pygame.event.get():  # Слежка🤓
        if event.type == pygame.QUIT:
            run = False
    all_sprites.update()  # update

    # рендеринг
    screen.fill((0, 0, 0)) #фон
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()