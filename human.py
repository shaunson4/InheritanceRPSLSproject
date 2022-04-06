from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = input ('Select a gesture: ')
        return super().choose_gesture()
       
