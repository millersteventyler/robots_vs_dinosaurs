class Dinosaur:
    def __init__(self, dinosaur_type, attack_power):
        self.dinosaur_type = dinosaur_type
        self.energy = 100
        self.attack_power = attack_power
        self.health = 100

    def dinosaur_attack_robot(self, robot):
        robot.health -= self.attack_power
        print(f'{self.dinosaur_type} attacks {robot.name} for {self.attack_power} damage. New health is {robot.health}')
