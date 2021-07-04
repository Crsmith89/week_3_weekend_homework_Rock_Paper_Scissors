from flask import render_template, redirect
from app import app
from models.player import Player
from models.game import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def start():
    return render_template('play.html')

@app.route('/<player1_choice>/<player2_choice>')
def play(player1_choice, player2_choice):
    player_1 = Player("Player 1", player1_choice)
    player_2 = Player("Player 2", player2_choice)
    game = Game()
    result = game.play_game(player_1, player_2)
    print(result)
    return render_template('index.html', title='Home', player1=player_1, player2=player_2, result=result)

