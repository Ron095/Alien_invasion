import pygame
class Ship():
    def __int__(self, screen):
        #Initialize the ship and set its starting position
        self.screen = screen

        #Load the ship image an get its rect.
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen