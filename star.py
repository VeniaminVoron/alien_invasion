import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Класс спрайтовой звезды."""
    def __init__(self, ai_settings, screen):
        """Инициализирует звезду и задает ее позицию."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Создание звезды в позиции 0, 0.
        self.rect = pygame.Rect(0, 0, ai_settings.star_width,
            ai_settings.star_height)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Сохранение точной позиции звезды.
        self.x = float(self.rect.x)
        
        self.color = ai_settings.star_color
        
    def draw_star(self):
        """Выводит звезду на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
