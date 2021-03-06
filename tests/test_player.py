import unittest

from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Andrew", "scissors")
            
    def test_player_has_name(self):
        self.assertEqual("Andrew", self.player_1.name)

    def test_player_has_move(self):
        self.assertEqual("scissors", self.player_1.move)
