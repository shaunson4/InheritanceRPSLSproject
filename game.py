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
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.select_gesture()
            self.compare_gestures()
        if self.player_one.score >= 2:
            print('Player One WINS the GAME!')
        else:
            print('Player Two WINS the GAME!')
        print('THE END, Thanks for playing!')
            
       

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
    
    def compare_gestures(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print('Tie round, start again')
        elif self.player_one.chosen_gesture == 'Rock' and (self.player_two.chosen_gesture == 'Scissors'or self.player_two.chosen_gesture == 'Lizard'):
            self.player_one.score += 1
            print('Player one wins Round!')
        elif self.player_one.chosen_gesture == 'Scissors' and (self.player_two.chosen_gesture == 'Paper'or self.player_two.chosen_gesture == 'Lizard'):
            self.player_one.score += 1
            print('Player one wins Round!')
        elif self.player_one.chosen_gesture == 'Paper' and (self.player_two.chosen_gesture == 'Rock'or self.player_two.chosen_gesture == 'Spock'):
            self.player_one.score += 1
            print('Player one wins Round!')
        elif self.player_one.chosen_gesture == 'Lizard' and (self.player_two.chosen_gesture == 'Paper'or self.player_two.chosen_gesture == 'Spock'):
            self.player_one.score += 1
            print('Player one wins Round!')
        elif self.player_one.chosen_gesture == 'Spock' and (self.player_two.chosen_gesture == 'Rock'or self.player_two.chosen_gesture == 'Scissors'):
            self.player_one.score += 1
            print('Player one wins Round!')
        else:
            self.player_two.score += 1
            print('Player Two wins Round!')
 
        


