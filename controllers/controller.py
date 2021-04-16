from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route("/game")
def index():
    return "Welcome to Rock Paper Scissors!"

@app.route("/game/<player1move>/<player2move>")
def play_game(player1move, player2move):
    player1 = Player("Player 1", player1move)
    player2 = Player("Player 2", player2move)
    game = Game(player1, player2)
    result = game.play_game()
    return render_template("index.html", result = result)
