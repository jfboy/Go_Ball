from math import pi, sin, cos

import pygame
from pygame.sprite import Sprite

class Ball(Sprite):

    def __init__(self,screen,game_setting,play_board):

        super().__init__()

        self.screen = screen
        self.game_setting = game_setting
        self.play_board = play_board

        self.screen_rect = self.screen.get_rect()
        self.ball_speed = game_setting.ball_speed
        self.ball_radius = self.game_setting.ball_radius
        self.ball_color = self.game_setting.ball_color
        self.direction = float(self.game_setting.ball_direction)
        self.rect = pygame.Rect(0,0,self.ball_radius,self.ball_radius)
        self.ball_rect = self.rect
        self.ball_rect.centerx = self.play_board.play_board_rect.centerx
        self.ball_rect.centery = self.play_board.play_board_rect.centery - \
                                 self.game_setting.play_board_height // 2 - self.ball_radius

        self.x, self.y = float(self.ball_rect.centerx), float(self.ball_rect.centery) #用于精细控制

    def creat(self):
        pygame.draw.ellipse(self.screen, self.ball_color, self.ball_rect)

    def update_index(self):#通过改变self.game_setting.ball_direction改变小球运动方向，共六种
        angle = (self.direction % 360 ) / 180 * pi
        self.x += ( self.game_setting.ball_speed * sin(angle) )
        self.y -= ( self.game_setting.ball_speed * cos(angle) )
        self.ball_rect.centerx = self.x
        self.ball_rect.centery = self.y

    def center(self): #使小球居于玩家挡板中央
        self.x = self.play_board.x
        self.y = self.play_board.play_board_rect.centery - \
                                 self.game_setting.play_board_height // 2 - self.ball_radius






