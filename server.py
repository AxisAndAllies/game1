import json
from flask import Flask, request
from game import Game

app = Flask(__name__)
only_game = Game()


@app.route('/game/<int:game_id>', methods=["GET"])
def find_game(game_id):
    msg = f"Game {game_id} doesn't exist yet!!"
    return msg


@app.route('/state', methods=["GET"])
def game_state():
    return json.dumps(only_game.get_state())


@app.route('/move', methods=["POST"])
def move():
    data = request.json
    num = _check_valid_num(data['num'])
    node_index_from = _check_valid_node(data["from"])
    node_index_to = _check_valid_node(data["to"])
    try:
        only_game.move(num, node_index_from, node_index_to)
    except Exception as e:
        return str(e), 400

    return json.dumps(only_game.get_state())


@app.route('/end_turn', methods=["POST"])
def end_turn():
    only_game.next_turn()
    return 'ended.'


def _check_valid_num(stuff):
    return int(stuff)


def _check_valid_node(stuff):
    return int(stuff)


@app.route('/add', methods=["POST"])
def reinforce():
    data = request.json
    num = _check_valid_num(data['num'])
    node_index = _check_valid_node(data["to"])
    try:
        only_game.reinforce(num, node_index)
    except Exception as e:
        return str(e), 400
    return json.dumps(only_game.get_state())