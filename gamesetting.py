# 游戏设置类
class Setting():

    def __init__(self):

        self.reset()

        #屏幕设置
        self.screen_wight = 600
        self.screen_height = 600
        self.bg_color = (227,211,157) #中金色

        #玩家挡板设置
        self.play_board_wight = 120
        self.play_board_height = 12
        self.play_board_color = (144,80,7) #胡萝卜色


        #小球设置
        self.ball_radius = 10
        self.ball_color = (0, 0, 255)#蓝色
        self.ball_direction = 0 #运动方向控制，单位为度，0为默认朝上，顺时针增大

        # 速度的增长率
        self.speed_increase_rate = 1.1

        #目标板初始设置
        self.aim_board_wight = 80
        self.aim_board_height = 20
        self.aim_board_space = 5
        self.aim_board_color = (172,55,19) #深珊瑚色
        self.space_rate = 0.25 #目标板所占区域的百分比

        #游戏得分板初始设置
        self.score = 0
        self.play_board_life = 8
        self.game_level = 1
        self.point_increase_rate = 1.5 #点数增长率

    def increase(self): #随着游戏进行需要改变的东西
        self.ball_speed *= self.speed_increase_rate
        self.play_board_speed *= self.speed_increase_rate
        self.aim_board_point = int(self.aim_board_point * self.point_increase_rate)

    def reset(self): #重开需要重置的东西
        self.play_board_speed = 0.8 #玩家挡板速度
        self.ball_speed = 0.8 #小球速度
        self.aim_board_point = 10 #目标挡板点数


