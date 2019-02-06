class Settings():
    """  储存游戏的所有设置的类"""

    def __init__(self):
        """ 初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        # 设置背景色
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # # 未消失的子弹数上限
        self.bullet_allowed = 5

        # 外球人的设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右，-1为向左
        self.fleet_direction = 1


