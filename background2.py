import pygame

from pygame.sprite import Sprite


class Background2 (Sprite):

    def __init__(self, ai_settings, screen):

        super(Background2, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/background2.jpg')
        self.rect = self.image.get_rect()

        self.y = float(self.rect.y)
        self.y -= 720

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        self.y += self.ai_settings.background_speed_factor
        self.rect.y = self.y
