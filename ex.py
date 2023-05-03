import pygame

# Initialize pygame
pygame.init()

# Set the window size and create the window
window_size = (800, 800)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Gun and Bullet Example')

# Load the images to use for the gun and bullet
gun_image = pygame.image.load('ship.bmp')
bullet_image = pygame.image.load('ship.bmp')

# Create a sprite class for the gun
class Gun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = gun_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bullets = pygame.sprite.Group()

    def fire(self):
        # Create a new bullet and add it to the sprite group
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.add(bullet)

# Create a sprite class for the bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Create an instance of the Gun class
gun = Gun(window_size[0] // 2, window_size[1] - 50)

# Create a sprite group to hold the gun and bullets
sprites = pygame.sprite.Group()
sprites.add(gun)

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_SPACE:
            gun.fire()

    # Update the sprites
    sprites.update()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the sprites
    sprites.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
