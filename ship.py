import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, screen,ai):
        super().__init__()
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.set = ai

        # Load the ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.image = pygame.transform.scale(self.image, (70,75))
        self.img_height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()


        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        """making a flag becasue to move it continus"""
        self.move_r = False
        self.move_l = False





    def update(self):
        if self.move_r and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.set.ship_sped
        if self.move_l and self.rect.left > 0:
            self.rect.centerx -= self.set.ship_sped

    def center_ship(self):
        self.center = self.screen_rect.centerx


    def blitme(self):
        self.screen.blit(self.image,self.rect)
        pygame.display.flip()