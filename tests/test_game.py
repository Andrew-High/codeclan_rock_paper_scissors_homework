import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Andrew", "scissors")
        self.player_2 = Player("Simon", "paper")
        self.player_3 = Player("Richard", "rock")
        self.game = Game(self.player_1, self.player_2)
    
    def test_game_has_players(self):
        self.assertEqual("Andrew", self.game.player_1.name)
        self.assertEqual("Simon", self.game.player_2.name)

    def test_scissors_wins_against_paper(self):
        self.assertEqual("Player 1 wins!", self.game.play_game(self.player_1, self.player_2))

    def test_paper_wins_against_rock(self):
        self.assertEqual("Player 2 wins!", self.game.play_game(self.player_3, self.player_2))

    def test_rock_wins_against_scissors(self):
        self.assertEqual("Player 1 wins!", self.game.play_game(self.player_3, self.player_1))