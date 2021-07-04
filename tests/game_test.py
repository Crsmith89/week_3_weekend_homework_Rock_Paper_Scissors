import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.rock = Player("Roosa", "rock")
        self.paper = Player("Colin", "paper")
        self.scissors = Player("Hannah", "scissors")

    def test_decide_rock_and_scissors(self):
        result = play_game(self.rock, self.scissors)
        self.assertEqual("Player 1 wins by playing rock", result)
        
    def test_decide_scissors_and_rock(self):
        result = play_game(self.scissors, self.rock)
        self.assertEqual("Player 2 wins by playing rock", result)
        
    def test_decide_paper_and_scissors(self):
        result = play_game(self.paper, self.scissors)
        self.assertEqual("Player 2 wins by playing scissors", result)

    def test_decide_scissors_and_paper(self):
        result = play_game(self.scissors, self.paper)
        self.assertEqual("Player 1 wins by playing scissors", result)
        
    def test_decide_rock_and_paper(self):
        result = play_game(self.rock, self.paper)
        self.assertEqual("Player 2 wins by playing paper", result)

    def test_decide_paper_and_rock(self):
        result = play_game(self.paper, self.rock)
        self.assertEqual("Player 1 wins by playing paper", result)

    def test_decide_paper_draw(self):
        result = play_game(self.paper, self.paper)
        self.assertEqual("No winner, this game is a draw", result)

    def test_decide_rock_draw(self):
        result = play_game(self.rock, self.rock)
        self.assertEqual("No winner, this game is a draw", result)
        
    def test_decide_scissors_draw(self):
        result = play_game(self.scissors, self.scissors)
        self.assertEqual("No winner, this game is a draw", result)