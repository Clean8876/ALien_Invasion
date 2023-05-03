import pygame.font
from pygame.sprite import Group
from ship import Ship

class Score_board:
    def __init__(self,screen,ai,stat):
        self.screen = screen
        self.set = ai
        self.screen_rect = self.screen.get_rect()
        self.stats = stat
        self.txt_col =(30,30,30)
        self.bg_col = (125,125,125)
        self.font = pygame.font.SysFont(None,48)
        self.scoring()
        self.high_sc()
        self.level()
        self.ship()


    def scoring(self):
        self.round = int(round(self.stats.score,-1))
        self.score = "{: ,}".format(self.round )
        self.score_img = self.font.render("SCORE "+self.score,True,self.txt_col,self.bg_col)
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def high_sc(self):
        self.round_sc = int(round(self.stats.highsc,-1))
        self.hig_score = "{: ,}".format(self.round_sc)
        self.high_scr = self.font.render("HIGHSCORE "+self.hig_score,True,self.txt_col,self.bg_col)
        self.high_scr_rect = self.high_scr.get_rect()
        self.high_scr_rect.centerx = self.screen_rect.centerx
        self.high_scr_rect.top = self.score_img_rect.top

    def level(self):
        self.level_img = self.font.render("Level "+ str(self.stats.level),True,self.txt_col,self.bg_col)
        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.right = self.score_img_rect.right
        self.level_img_rect.top = self.score_img_rect.bottom + 10

    def ship(self):
        self.ships = Group()
        for grp_ship in range(self.stats.ship_left):
            ship = Ship(self.screen,self.stats)
            ship.rect.x = 5 + grp_ship * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)



    def draw(self):
        self.screen.blit(self.high_scr, self.high_scr_rect)
        self.screen.blit(self.score_img,self.score_img_rect)
        self.screen.blit(self.level_img,self.level_img_rect)
        self.ships.draw(self.screen)



