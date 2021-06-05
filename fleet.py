from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot1 = Robot('Killer')
        robot2 = Robot('Slasher')
        robot3 = Robot('Apple')
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
