import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Загрузка изображения корабля и получения прямоугольника.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Сохранение вещественной координаты центера корабля.
        self.center_0 = float(self.rect.centerx)
        self.center_1 = float(self.rect.centery)
        # Флаг перемещения.
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
        
    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляется атрибут center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_0 += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_0 -= self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.center_1 -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.center_1 += self.ai_settings.ship_speed_factor
            
        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center_0
        self.rect.centery = self.center_1
            
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.center = self.screen_rect.centerx
