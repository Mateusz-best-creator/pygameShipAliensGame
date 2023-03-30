import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullets(Sprite):
    
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.sett = Settings()
        self.settings = ai_game.settings
        self.color = self.sett.bullet_color

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0, self.sett.bullet_width,self.sett.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        self.y=float(self.rect.y)

    def update(self):
        """Move the bullet up to the screen"""
        self.y -= self.sett.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet up to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
