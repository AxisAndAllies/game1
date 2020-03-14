from flask import Flask
from risk import Risk

app = Flask(__name__)

only_game = Risk()

def render(risk: Risk):
    return risk.state

@app.route('/game/<int:game_id>', methods=["GET"])
def find_game(game_id):
    msg = f"Game {game_id} doesn't exist yet!!"
    return msg
    
@app.route('/state')
def game_state():
    return 'Hello, World!'

@app.route('/move', methods=["POST"])
def move():

    return 'moved.'

@app.route('/end_turn', methods=["POST"])
def end_turn():
    return 'ended.'

@app.route('/reinforce', methods=["POST"])
def reinforce():
    return 'reinforced.'