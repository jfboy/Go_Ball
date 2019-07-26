import sys
from time import sleep
from aim_board import Aim_board
import pygame

#刷新屏幕
def update_screen(game_setting,screen,play_board,ball,aim_boards,sb):
    screen.fill(game_setting.bg_color)
    sb.show()
    play_board.creat()
    ball.creat()
    aim_boards.draw(screen)
    pygame.display.flip()

# 监控按键事件
def check_events(game_setting,play_board,change):
    # 监控按键事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #响应退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 响应键盘按下
            if event.key == pygame.K_SPACE:
                if not change.pause:
                    change.pause = True
                if not change.start:
                    change.start = True
            elif event.key == pygame.K_RIGHT:
                if change.start:
                    if change.pause:
                        change.pause = False
                    play_board.right = True
            elif event.key == pygame.K_LEFT:
                if change.start:
                    if change.pause:
                        change.pause = False
                    play_board.left = True

        elif event.type == pygame.KEYUP:  # 响应键盘松开
            if event.key == pygame.K_RIGHT:
                play_board.right = False
            elif event.key == pygame.K_LEFT:
                play_board.left = False

#检查小球与屏幕边缘、玩家挡板、目标挡板的碰撞并做出相应的处理
def check_ball_collision(screen,game_setting,play_board, ball, aim_boards,sb,change):
    screen_rect = screen.get_rect()
    play_board_rect = play_board.play_board_rect
    ball_rect = ball.ball_rect
    angle = ball.direction
    # 撞到玩家挡板
    if ball_rect.bottom > play_board_rect.top and (ball_rect.left > play_board_rect.left and ball_rect.right < play_board_rect.right):
        if change.start:
            bias = (ball_rect.centerx - play_board_rect.centerx) / (0.5 * change.play_board_wight) * 20
            angle = 540 - angle + bias

    #撞到四壁
    if screen_rect.left >= ball_rect.left: #左壁
        angle = 360 - angle
    elif ball_rect.right >= screen_rect.right: #右壁
        angle = 360 - angle
    elif screen_rect.top >= ball_rect.top: #顶部
        angle = 540 - angle
    elif ball_rect.bottom >= screen_rect.bottom: #底部
        angle = center_pause(change,play_board,ball) #归中暂停
        change.play_board_life -= 1 #生命减一
        sb.pre_life()
        #当玩家生命值减完
        if change.play_board_life <= 0:
            change.start = False #游戏结束
            game_setting.reset()
            change.reset()
            aim_boards.empty()
            sb.pre()
            creat_aim_board_fleet(game_setting,screen_rect,aim_boards,change) #开始新的一轮
        sleep(0.5)

    #撞到目标挡板
    collosion = pygame.sprite.spritecollide(ball,aim_boards,True)
    if collosion:
        angle = 540 - angle
        aim_boards.remove(collosion)
        change.score += game_setting.aim_board_point * len(collosion)
        sb.pre_score()
        check_high_score(change,sb)

    # 当全部被消灭后的处理
    if len(aim_boards) <= 0:
        change.game_level += 1
        sb.pre_level()
        game_setting.increase()
        angle = center_pause(change,play_board,ball) #归中暂停
        creat_aim_board_fleet(game_setting, screen, aim_boards,change)

    ball.direction = angle #改变方向,最重要

def center_pause(change,play_board,ball):
    angle = 0
    change.pause = True
    play_board.center()
    ball.center()
    return angle

#检查是否产生最高分
def check_high_score(change,sb):
    if change.score > change.high_score:
        change.high_score = change.score
        with open('high_score.txt', 'wt') as f:
            f.write(str(change.high_score))
            sb.pre_high_score()

#创建一群目标板
def creat_aim_board_fleet(game_setting,screen,aim_boards,change):

    #计算每一行，每一列能放多少个目标板
    rows = (game_setting.screen_height - game_setting.play_board_height - (1-change.space_rate)*game_setting.screen_height) \
           // (game_setting.aim_board_height + game_setting.aim_board_space)
    colums = (game_setting.screen_wight - game_setting.aim_board_space) // \
             (game_setting.aim_board_wight + game_setting.aim_board_space)
    space = (game_setting.screen_wight - colums*(game_setting.aim_board_wight + game_setting.aim_board_space) ) // colums
    new_space = space + game_setting.aim_board_space #重新规划每一列之间的间隔

    #创建目标板并放在相应位置
    for row in range(int(rows)):
        for colum in range(colums):
            aim_board  = Aim_board(game_setting,screen)
            aim_board.rect.x = colum * (game_setting.aim_board_wight + new_space) + \
                                         new_space #使用新间隔
            aim_board.rect.y = row * (game_setting.aim_board_height + game_setting.aim_board_space) + \
                                         game_setting.aim_board_space
            aim_boards.add(aim_board)







