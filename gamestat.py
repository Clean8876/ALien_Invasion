class Game_stat():
    def __init__(self):
        self.highsc = 0
        self.shp = 3
        self.level = 0
        self.reset()
        self.game_act = False



    def reset(self):
        self.ship_left = self.shp
        self.score = 0
