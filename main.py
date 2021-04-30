import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self,image,screen):
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = 600
