class Settings():
    """  储存游戏的所有设置的类"""

    def __init__(self):
        """ 初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 480
        self.screen_height = 720
        # 设置背景色
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_width = 5
        self.bullet_height = 18
        self.bullet_color = 40, 40, 40
        # # 未消失的子弹数上限
        self.bullet_allowed = 10

        # 外球人的设置
        self.fleet_drop_speed = 10

        # 背景图片的设置
        self.background_speed_factor = 8

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 飞船的设置
        self.ship_speed_factor = 5
        # 子弹的设置
        self.bullet_speed_factor = 4
        # 外球人的设置
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右，-1为向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        # self.ship_speed_factor *= self.speedup_scale
        # self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
