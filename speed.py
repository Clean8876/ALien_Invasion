class Speed:
    def __init__(self):
        self.al_drop = 10
        self.multipy = 1.1
        self.alien_mlt = 1.5
        self.intial_speed()

    def intial_speed(self):
        self.ship_sped = 1.5
        self. bult= 3
        self.alien_drct = 1
        self.alien_sped = 1.0
        self.alien_sht = 50

    def increase_speed(self):
        self.ship_sped *= self.multipy
        self.bult *= self.multipy
        self.alien_sped *= self.multipy
        self.alien_drct *= self.multipy
        self.alien_sht = int(self.alien_sht * self.alien_mlt)

