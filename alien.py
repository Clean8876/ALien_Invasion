import pygame
from  pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen,ai):
        super().__init__()
        self.screen = screen
        self.scren_rect = self.screen.get_rect()
        self.set = ai
        self.image = pygame.image.load('ali.bmp')
        self.rect =  self.image.get_rect()
        self.speed_factor = 1.0
        self.fleet_direction = 1
        self.drop_direction = 10

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edge(self):
        if self.rect.right >= self.scren_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x +=( self.set.alien_sped * self.set.alien_drct)
        self.rect.x = self.x

