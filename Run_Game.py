import pygame
import sys
from ship import Ship
from bullet import Bullet
from  alien import Alien
from  gamestat import Game_stat
from button import Button
from speed import Speed
from score import Score_board
from time import sleep
"""after imorting pygame lib """
class Game:
    def __init__(self):
        pygame.init()
        """AFter intitalize the pygame set the screen size and the bg colour"""
        self.screen_width =  1200
        self.screen_height = 800
        self.bg_color = (125,125,125)
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.speed = float(3.5)
        self.ai = Speed()
        self.stat = Game_stat()
        self.ship = Ship(self.screen,self.ai)
        self.sc = Score_board(self.screen, self.ai, self.stat)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.play = Button(self.screen)
        self.create_fleet()

        pygame.display.set_caption("Alien Invasion")

        """Create group and put bullet in a spirte group to movement"""

    def run_game(self):

        """Run the game"""
        while True:
            if self.stat.game_act:

                self.ship.update()
                self._update_bullets()
                self.update_alien()
            self.update_screen()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                           if event.key == pygame.K_q:
                                sys.exit()
                           if event.key == pygame.K_a:
                               self.ship.move_l = True
                           elif event.key == pygame.K_d:
                               self.ship.move_r = True
                           elif event.key == pygame.K_SPACE:

                               if len(self.bullets) < 3:
                                   new_bullet = Bullet(self.screen,self.ai,self.ship)
                                   self.bullets.add(new_bullet)

                elif event.type == pygame.KEYUP:
                           if event.key == pygame.K_a:
                               self.ship.move_l = False
                           elif event.key == pygame.K_d:
                               self.ship.move_r = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x ,mouse_y = pygame.mouse.get_pos()
                    butclk = self.play.rect.collidepoint(mouse_x,mouse_y)
                    if butclk and not self.stat.game_act:
                        self.stat.game_act = True
                        self.stat.reset()
                        self.sc.level()
                        self.sc.high_sc()
                        self.sc.scoring()
                        self.sc.ship()
                        self.ai.intial_speed()
                        pygame.mouse.set_visible(False)
                        """empty alien"""
                        self.aliens.empty()
                        self.bullets.empty()
                        self.create_fleet()
                        self.ship.center_ship()






    def create_fleet(self):
        alien = Alien(self.screen,self.ai)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        self.space = self.screen_width - (2 * alien_width)
        aliennum = self.space // (2 * alien_width)

        """create arow fo alien"""
        self.ship_height = self.ship.rect.height
        self.spacey = self.screen_height - ((3 * alien_height - self.ship_height))
        number_row = self.spacey // (2* alien_height)

        for row_number in range(number_row):
            for aliennus in range(aliennum):
                self._createalien(aliennus,row_number)
            """put it in rowe"""

    def _createalien(self,aliennus,row_number):
        alien = Alien(self.screen,self.ai)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * aliennus
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.fleet_direction()
                break

    def fleet_direction(self):

        for alien in self.aliens.sprites():
            alien.rect.y += self.ai.al_drop
        self.ai.alien_drct *= -1

    def update_alien(self):
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self.ship_hit()
        self.alien_drop()
        self._fleet_edges()


    def _update_bullets(self):
        self.bullets.update()
        for self.amo in self.bullets.copy():
            if self.amo.rect.bottom <= 0:
                self.bullets.remove(self.amo)
        self.collision_bullete_and_Alien()

    def collision_bullete_and_Alien(self):
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collision:
            for alien in collision.values():
                self.stat.score += self.ai.alien_sht * len(alien)
                self.sc.scoring()
            self.check_high_sc()
        if not self.aliens:
            self.bullets.empty()
            self.ai.increase_speed()
            self.stat.level += 1
            self.sc.level()
            self.create_fleet()

    def check_high_sc(self):
        if self.stat.score > self.stat.highsc:
            self.stat.highsc = self.stat.score
            self.sc.high_sc()

    def ship_hit(self):
        if self.stat.ship_left > 0:
            self.stat.ship_left -= 1
            self.sc.ship()
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stat.game_act = False
            pygame.mouse.set_visible(True)

    def alien_drop(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break



    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.aliens.draw(self.screen)
        self.sc.draw()

        if not self.stat.game_act:
            self.play.draw_but()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        pygame.display.flip()




game = Game()
game.run_game()
