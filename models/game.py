class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self):
        if self.player_1.move == "rock" and self.player_2.move == "scissors":
            return "Player 1 wins!"
        elif self.player_1.move == "rock" and self.player_2.move == "paper":
            return "Player 2 wins!"
        elif self.player_1.move == "scissors" and self.player_2.move == "paper":
            return "Player 1 wins!"
        elif self.player_1.move == "scissors" and self.player_2.move == "rock":
            return "Player 2 wins!"
        elif self.player_1.move == "paper" and self.player_2.move == "rock":
            return "Player 1 wins!"
        elif self.player_1.move == "paper" and self.player_2.move == "scissors":
            return "Player 2 wins!"
        elif self.player_1.move == self.player_2.move:
            return "It's a draw!"
        else:
            return "Please input a valid game"
        
            