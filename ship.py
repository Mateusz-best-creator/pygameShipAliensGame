import pygame
from settings import Settings
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_game):
        """A class to manage the ship"""
        super().__init__()
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.image=pygame.image.load("./ship.jpg")
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom

        self.move_right=False
        self.move_left=False
        self.move_up=False
        self.move_down=False

        self.sett=Settings()
        self.speed=self.sett.ship_speed

    def update(self):

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x+=self.speed
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.rect.x-=self.speed-0.2
        if self.move_up and self.rect.y > 0:
            self.rect.y-=self.speed-0.2
        if self.move_down and self.rect.y < 750:
            self.rect.y+=self.speed
        #print(self.rect.y)

    def blitme(self):
        """Draw a ship"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)