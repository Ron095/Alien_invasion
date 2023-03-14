import pygame
class Ship():
    def __init__(self, screen):
        #Initialize the ship and set its starting position
        self.screen = screen

        #Load the ship image an get its rect.
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Movement flag
        self.moving_right = False
        self.moving_left = False

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        #Update the ship's position based on the movement flag
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitime(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)