from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print('Welcome to Robots VS. Dinosaurs, only one team will win!')

    def battle(self):
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            self.robo_turn()
            if len(self.herd.dinosaurs) > 0:
                self.dino_turn()

    def dino_turn(self):
        print("Dinosaur's turn! Choose a dinosaur to attack and a robot to defend")
        self.show_dinosaur_opponent_options()
        chosen_dino = int(input())
        self.show_robot_opponent_options()
        chosen_robot = int(input())
        self.herd.dinosaurs[chosen_dino].dinosaur_attack_robot(self.fleet.robots[chosen_robot])
        if self.fleet.robots[chosen_robot].health <= 0:
            print(f'{self.fleet.robots[chosen_robot].name} has died.')
            self.fleet.robots.remove(self.fleet.robots[chosen_robot])

    def robo_turn(self):
        print("Robot's turn! Choose a robot to attack and a dinosaur to defend")
        self.show_robot_opponent_options()
        chosen_robot = int(input())
        self.show_dinosaur_opponent_options()
        chosen_dino = int(input())
        self.fleet.robots[chosen_robot].robot_attack_dinosaur(self.herd.dinosaurs[chosen_dino])
        if self.herd.dinosaurs[chosen_dino].health <= 0:
            print(f'{self.herd.dinosaurs[chosen_dino].dinosaur_type} has died.')
            self.herd.dinosaurs.remove(self.herd.dinosaurs[chosen_dino])

    def show_dinosaur_opponent_options(self):
        print('Choose a dinosaur:')
        dino_index = 0
        for dino in self.herd.dinosaurs:
            print(f'Press {dino_index} for {dino.dinosaur_type}')
            dino_index += 1

    def show_robot_opponent_options(self):
        print('Choose a robot:')
        robot_index = 0
        for robo in self.fleet.robots:
            print(f'Press {robot_index} for {robo.name}')
            robot_index += 1

    def display_winners(self):
        if len(self.fleet.robots) > 0:
            print('Robots win!')
        else:
            print('Dinosaurs win!')
