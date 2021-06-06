from weapon import Weapon


class Robot:
    def __init__(self, robot_name):
        self.name = robot_name
        self.power_level = 100
        self.health = 100
        self.weapon = Weapon("Rocket", 100)

    def robot_attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f'{self.name} attacks {dinosaur.dinosaur_type} with a {self.weapon.weapon_type} for {self.weapon.attack_power} damage. New health is {dinosaur.health}')
