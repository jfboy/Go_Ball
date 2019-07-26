import pygame
from pygame.sprite import Group
from PIL import Image
from gamesetting import Setting
from play_board import Play_board
from ball import Ball
import game_function as gf
from score_board import Score_board
from game_change import Game_change

def run_game():

    pygame.init() #初始化
    game_setting = Setting() #创建一个设置类对象
    screen = pygame.display.set_mode((game_setting.screen_wight, game_setting.screen_height))# 创建一个屏幕对象
    pygame.display.set_caption("Go_Ball")
    change = Game_change(game_setting) #统计游戏中的变化信息的对象
    play_board = Play_board(screen,game_setting,change)#创建一个玩家挡板对象
    ball = Ball(screen,game_setting,play_board)#创建一个小球
    sb = Score_board(game_setting,screen,change) #创建一个记分板
    #建一个目标板图像文件
    image = Image.new('RGB', (game_setting.aim_board_wight, game_setting.aim_board_height), game_setting.aim_board_color)
    image.save('aim_board.bmp')
    aim_boards= Group() #创建一个目标板编组
    gf.creat_aim_board_fleet(game_setting,screen,aim_boards,change) #创建一群目标板


    #游戏主循环
    while True:

        gf.update_screen(game_setting, screen, play_board, ball, aim_boards, sb) #刷新屏幕

        gf.check_events(game_setting,play_board,change) #监控键盘事件

        if change.start:

            if not change.pause:

                gf.check_ball_collision(screen, game_setting, play_board, ball, aim_boards, sb,change)  # 监控小球的碰撞并做出处理

                play_board.update_index() #更新玩家挡板位置

                ball.update_index() #更新小球位置

if __name__ == '__main__':
    run_game()