#!/user/bin/env python
# -*- coding: utf-8 -*-

'bullet moudle'
__author__ = 'lazyChen'

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''在飞船所处的位置创建一个子弹对象'''
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        
        #在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        '''向上移动子弹'''
        #更新表示子弹位置的小树值
        self.y -= self.speed_factor
        #更新拜师子弹的rect的位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
               