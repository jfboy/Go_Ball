import pygame

class Score_board():

    def __init__(self,game_setting,screen,change):

        self.game_setting = game_setting
        self.screen = screen
        self.change = change
        self.screen_rect = self.screen.get_rect()

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)  # 文本
        self.font = pygame.font.SysFont('SimHei', 18)  # 字体,字号，得分信息
        self.font_2 = pygame.font.SysFont('SimHei', 12)  # 字体,字号，提示信息

        self.pre()

    def pre(self):
        self.pre_score()
        self.pre_high_score()
        self.pre_level()
        self.pre_life()
        self.pre_tip_1()
        self.pre_tip_2()

     # 将得分转化为一幅渲染的图像、并将得分放在屏幕左下角
    def pre_score(self):
        score_str = "当前得分:" + str(self.change.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left
        self.score_rect.bottom = self.screen_rect.bottom - 0.25*self.game_setting.screen_height

     # 将最高分转化为一幅渲染的图像、并将最高分放在得分上方
    def pre_high_score(self):
        high_score_str = "最高分:" + str(self.change.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.game_setting.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.score_rect.left
        self.high_score_rect.bottom = self.score_rect.top - 5

    # 将等级转化为一幅渲染的图像、并将等级放在最高分上方
    def pre_level(self):
        level_str = "等级:" + str(self.change.game_level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.game_setting.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.bottom = self.high_score_rect.top - 5

    # 将生命转化为一幅渲染的图像、并将生命放在等级上方
    def pre_life(self):
        life_str = "生命:" + str(self.change.play_board_life)
        self.life_image = self.font.render(life_str, True, self.text_color, self.game_setting.bg_color)
        self.life_rect = self.life_image.get_rect()
        self.life_rect.left = self.score_rect.left
        self.life_rect.bottom = self.level_rect.top - 5

    # 将提示转化为一幅渲染的图像、并将提示放在生命上方
    def pre_tip_1(self):
        tip_str = "左/右键:控制左/右,解除暂停,发射小球"
        self.tip_image_2 = self.font_2.render(tip_str, True, self.text_color, self.game_setting.bg_color)
        self.tip_rect_2 = self.tip_image_2.get_rect()
        self.tip_rect_2.left = self.score_rect.left
        self.tip_rect_2.bottom = self.life_rect.top - 30
    def pre_tip_2(self):
        tip_str = "空格:开始/暂停"
        self.tip_image_1 = self.font_2.render(tip_str, True, self.text_color, self.game_setting.bg_color)
        self.tip_rect_1 = self.tip_image_1.get_rect()
        self.tip_rect_1.left = self.score_rect.left
        self.tip_rect_1.bottom = self.tip_rect_2.top - 5


    # 在屏幕上显示得分等信息
    def show(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.life_image, self.life_rect)
        self.screen.blit(self.tip_image_1, self.tip_rect_1)
        self.screen.blit(self.tip_image_2, self.tip_rect_2)


