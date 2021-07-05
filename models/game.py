from models.player import Player
import random

class Game:

    def play_game(self, player_1, player_2):

        if player_1.choice == "rock" and player_2.choice == "scissors":
            return "Winner, well done"
        elif player_1.choice == "rock" and player_2.choice == "rock":
            return "Draw!! we go again"
        elif  player_1.choice == "paper" and player_2.choice == "rock":
            return "Winner, well done"
        elif player_1.choice == "paper" and player_2.choice == "paper":
            return "DRAW!! we go again"
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            return "Winner, well done"
        elif player_1.choice == "scissors" and player_2.choice == "scissors":
            return "Draw!! we go again"
        else:
            return "Loooooser!"
            
# computer extensions
    def gen_computer_player(self):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        computer_choice = Player("Computer", computer_choice)        