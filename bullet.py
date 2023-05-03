# bullet.py
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen,ai,ship):
        # Initialize the bullet and set its starting position
        super().__init__()
        self.screen = screen
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = ai
        self.color = (160, 32, 240)


        # Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)



    def update(self):
        # Move the bullet up the screen
        self.y -= self.bullet_speed.bult
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw the bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)




