from weapon import Weapon


class Robot:
    def __init__(self, robot_name):
        self.name = robot_name
        self.power_level = 100
        self.health = 100
        self.weapon = Weapon("Rocket", 100)
