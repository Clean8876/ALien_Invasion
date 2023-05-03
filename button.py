import pygame.font

class Button:
    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()


        """make dimension for buttons"""
        self.width ,self.height = 200,50
        self.but_col = (255,255,255)
        self.but_txt = (0,255,0)
        self.font = pygame.font.SysFont(None,48)

        """build the button"""
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self.give_msg()


    def give_msg(self):
        self.play_image = self.font.render("PLAY",True,self.but_txt, self.but_col)
        self.play_image_rect = self.play_image.get_rect()
        self.play_image_rect.center = self.rect.center

    def draw_but(self):
        self.screen.fill(self.but_col,self.rect)
        self.screen.blit(self.play_image,self.play_image_rect)
