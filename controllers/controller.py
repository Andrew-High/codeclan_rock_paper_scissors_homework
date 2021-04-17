from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player
from random import random

@app.route("/game")
def index():
    return render_template("index.html")

@app.route("/game/two_player/<player1move>/<player2move>")
def play_game(player1move, player2move):
    player_1 = Player("Player 1", player1move)
    player_2 = Player("Player 2", player2move)
    game = Game(player_1, player_2)
    result = game.play_game()
    return render_template("index.html", result = result)

@app.route("/game/two_player")
def two_player_homepage():
    return render_template("two_player.html", result = "Play a game to get a result")

@app.route("/game/two_player", methods=["POST"])
def play_game_with_inputs():
    player_1 = Player(request.form["player1name"], request.form["player1move"])
    player_2 = Player(request.form["player2name"], request.form["player2move"])
    game = Game(player_1, player_2)
    result = game.play_game()
    return render_template("two_player.html", result = result)

@app.route("/game/single_player", methods=["GET"])
def single_player_homepage():
    return render_template("single_player.html", result = "Play a game to get a result")


@app.route("/game/single_player", methods=["POST"])
def play_game_with_computer():
    player_1 = Player(request.form["player1name"], request.form["player1move"])
    def computer_gesture():
        random_number = random()
        if random_number >= 0 and random_number < 0.33:
            return "rock"
        elif random_number >= 0.33 and random_number < 0.66:
            return "paper"
        elif random_number >= 0.66:
            return "scissors"
    player_2 = Player("Computer", computer_gesture())
    game = Game(player_1, player_2)
    result = game.play_game()
    return render_template("single_player.html", result = result)
    
