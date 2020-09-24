import os
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Инициализирует pygame, settings и объект экрана.
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    
    # Создание корабля, группы пуль, группы пришельцев, группы звезд.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stars = Group()
    
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Создание звезд.
    gf.create_stars(ai_settings, screen, stars)
    
    clock = pygame.time.Clock()
    FPS = 200
    
    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Запуск основного цикла игры.
    while True:
        clock.tick(FPS)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, 
                aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, 
                bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
            stars, play_button)
        
run_game()
