from player import Player
import random
class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.choosen_gesture = random.choice(self.chosen_gesture)
        



        

