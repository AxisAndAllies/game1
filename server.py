from flask import Flask, request, jsonify
from game import Game
app = Flask(__name__)

only_game = Game()

# def render(risk: Risk):
#     return risk.state


@app.route('/game/<int:game_id>', methods=["GET"])
def find_game(game_id):
    msg = f"Game {game_id} doesn't exist yet!!"
    return msg


@app.route('/state')
def game_state():
    return only_game.state


@app.route('/move', methods=["POST"])
def move():
    data = request.json
    num = data["num"]
    node_index_from = data["node_index_from"]
    node_index_to = data["node_index_to"]
    only_game.move(num, node_index_from, node_index_to)
    return 'moved.'


@app.route('/end_turn', methods=["POST"])
def end_turn():
    only_game.next_turn()
    return 'ended.'


@app.route('/reinforce', methods=["POST"])
def reinforce():
    data = request.json
    num = data["num"]
    node_index = data["node_index"]
    only_game.reinforce(num, node_index)
    return 'reinforced.'