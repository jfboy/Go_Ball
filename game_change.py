#统计游戏中的变化信息
class Game_change():

    def __init__(self,game_setting):

        self.game_setting = game_setting
        self.reset()

        # 游戏开始标志
        self.start = False
        # 游戏暂停标志
        self.pause = True

        with open('high_score.txt', 'rt') as f:
            self.high_score = int(f.readline())

    def reset(self):  # 游戏中需要重置的信息

        self.score = self.game_setting.score
        self.play_board_life = self.game_setting.play_board_life
        self.game_level = self.game_setting.game_level
        self.space_rate = self.game_setting.space_rate # 目标板所占区域的百分比
        self.play_board_wight = self.game_setting.play_board_wight
