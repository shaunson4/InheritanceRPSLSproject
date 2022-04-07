from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = input(f'Select a gesture from {self.list_of_possible_gestures}: ')
        
       
