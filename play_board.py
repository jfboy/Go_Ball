import pygame

class Play_board():

    def __init__(self,screen,game_setting,change):

        self.screen = screen
        self.game_setting = game_setting
        self.change = change

        self.play_board_wight = self.change.play_board_wight #可做动态宽度
        self.play_board_height = self.game_setting.play_board_height
        self.play_board_color = self.game_setting.play_board_color

        self.screen_rect = self.screen.get_rect()
        self.play_board_rect = pygame.Rect(0,0,self.play_board_wight,self.play_board_height)
        self.play_board_rect.centerx = self.screen_rect.centerx  # 放置底部中央
        self.play_board_rect.bottom = self.screen_rect.bottom

        self.right = False
        self.left = False

        self.x = float(self.play_board_rect.centerx)  # 精确控制

    def creat(self): #画出玩家挡板
        pygame.draw.rect(self.screen,self.play_board_color,self.play_board_rect)

    def update_index(self):#更新位置
        if self.right and self.play_board_rect.right < self.screen_rect.right:
             self.x += self.game_setting.play_board_speed
        if self.left and self.play_board_rect.left > self.screen_rect.left:
             self.x -= self.game_setting.play_board_speed
        self.play_board_rect.centerx = self.x

    def center(self): #使挡板居中
        self.x = self.screen_rect.centerx  # 放置底部中央

