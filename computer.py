from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):

        super().choose_gesture()
        self.chosen_gesture = random.choice (self.list_of_possible_gestures) 




        

