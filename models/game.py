from models.player import Player
import random

class Game:

    def play_game(self, player_1, player_2):

        if player_1.choice == "rock" and player_2.choice == "scissors":
            return "You win!!"
        elif player_1.choice == "rock" and player_2.choice == "rock":
            return "Draw!! go again"
        elif  player_1.choice == "paper" and player_2.choice == "rock":
            return "You win!!"
        elif player_1.choice == "paper" and player_2.choice == "paper":
            return "DRAW!! go again"
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            return "You WIN!"
        elif player_1.choice == "scissors" and player_2.choice == "scissors":
            return "Draw!! go again"
        else:
            return "Loooooser!"
        