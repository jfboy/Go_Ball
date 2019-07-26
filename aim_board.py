import pygame
from pygame.sprite import Sprite

class Aim_board(Sprite):

    def __init__(self,game_setting,screen):
        super().__init__()

        self.game_setting = game_setting
        self.screen = screen

        self.aim_board_wight = self.game_setting.aim_board_wight
        self.aim_board_height = self.game_setting.aim_board_height
        self.aim_board_color = self.game_setting.aim_board_color

        self.image = pygame.image.load('aim_board.bmp')
        self.rect = self.image.get_rect()

        #起初放在左上角附近
        self.rect.x = self.aim_board_wight
        self.rect.y = self.aim_board_height

    def creat(self):
        self.screen.blit(self.image,self.rect)


