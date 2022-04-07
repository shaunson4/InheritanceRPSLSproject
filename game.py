from human import Human
from computer import Computer
class Game():
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
       


    def run_game(self):
        print('Welcome to a game of Rock, Paper, Scissors, Lizzard, Spock!')
        print('Rule Key is as follows: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock ')   
        self.player_two_choice()
        self.select_gesture()

        # self.player_one.choose_gesture()

    def player_two_choice(self):
        opponent_choice = input('Do you want to play the computer? y/n: ')
        if opponent_choice == 'y':
            self.player_two = Computer()
            print('Player Two is the computer')
        else:
            self.player_two = Human()
            print('Player Two is also human')

    def select_gesture(self):
        print('Player One a Human, will select a gesture first!')
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        print(f' Player Two gesture is: {self.player_two.chosen_gesture}')
        


