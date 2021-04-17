class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self):
        if self.player_1.move == "rock" and self.player_2.move == "scissors":
            return f"{self.player_1.name} wins by playing rock, beating {self.player_2.name}'s scissors!!"
        elif self.player_1.move == "rock" and self.player_2.move == "paper":
            return f"{self.player_2.name} wins by playing paper, beating {self.player_1.name}'s rock!!"
        elif self.player_1.move == "scissors" and self.player_2.move == "paper":
            return f"{self.player_1.name} wins by playing scissors, beating {self.player_2.name}'s paper!!"
        elif self.player_1.move == "scissors" and self.player_2.move == "rock":
            return f"{self.player_2.name} wins by playing rock, beating {self.player_1.name}'s scissors!!"
        elif self.player_1.move == "paper" and self.player_2.move == "rock":
            return f"{self.player_1.name} wins by playing paper, beating {self.player_2.name}'s rock!!"
        elif self.player_1.move == "paper" and self.player_2.move == "scissors":
            return f"{self.player_2.name} wins by playing scissors, beating {self.player_1.name}'s paper!"
        elif self.player_1.move == self.player_2.move:
            return "It's a draw!"
        else:
            return "Please input a valid game"
        
            