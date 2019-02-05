import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外球人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外球人并设置其起始位置"""

        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外球人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外球人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外球人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外球人"""
        self.screen.blit(self.image, self.rect)
