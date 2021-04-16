import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Andrew", "scissors")
        self.player_2 = Player("Simon", "paper")
        self.player_3 = Player("Richard", "rock")
        self.player_4 = Player("Iain", "scissors")
        self.player_5 = Player("Morten", "banana")
        self.game_1 = Game(self.player_1, self.player_2)
        self.game_2 = Game(self.player_3, self.player_2)
        self.game_3 = Game(self.player_3, self.player_1)
        self.game_4 = Game(self.player_1, self.player_4)
    
    def test_game_has_players(self):
        self.assertEqual("Andrew", self.game_1.player_1.name)
        self.assertEqual("Simon", self.game_1.player_2.name)

    def test_scissors_wins_against_paper(self):
        self.assertEqual("Player 1 wins!", self.game_1.play_game())

    def test_paper_wins_against_rock(self):
        self.assertEqual("Player 2 wins!", self.game_2.play_game())

    def test_rock_wins_against_scissors(self):
        self.assertEqual("Player 1 wins!", self.game_3.play_game())

    def test_draw(self):
        self.assertEqual("It's a draw!", self.game_4.play_game())