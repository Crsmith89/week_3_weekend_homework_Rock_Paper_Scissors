from flask import render_template, request
from app import app
from models.player import Player
from models.game import *
import random

@app.route('/')
def index():
    return render_template('index.html', title='Rock Paper Scissors')

@app.route('/play')
def play():
    return render_template('play.html', title='Play')
# play against cpu
@app.route('/play', methods=['POST'])
def play_against_computer():
    name = request.form['name']
    choice = request.form['choice']
    player = Player(name=name, choice=choice)
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    computer = Player("Computer", computer_choice)
    game = Game()
    result = game.play_game(player, computer)
    print(result)
    return render_template('result.html', title='Rock Paper Scissors', player1=player, player2=computer, result=result)

@app.route('/rules')
def display_rules():
    return render_template('rules.html', title='Rules')

@app.route('/play/<player1_choice>/<player2_choice>')
def start(player1_choice, player2_choice):
    player_1 = Player("Player 1", player1_choice)
    player_2 = Player("Player 2", player1_choice)
    game = Game()
    result = game.play_game(player_1, player_2)
    print(result)
    return render_template('result.html', title='Rock Paper Scissors', player1=player_1, player2=player_2, result=result)

