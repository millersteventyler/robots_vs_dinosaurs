from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dinosaur1 = Dinosaur('T-Rex', 100)
        dinosaur2 = Dinosaur('velociraptor', 100)
        dinosaur3 = Dinosaur('Europasaurus', 100)
        self.dinosaurs.append(dinosaur1)
        self.dinosaurs.append(dinosaur2)
        self.dinosaurs.append(dinosaur3)
