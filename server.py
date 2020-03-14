from flask import Flask
app = Flask(__name__)

@app.route('/game/<int:game_id>')
def find_game(game_id):
    msg = f"Game {game_id} doesn't exist yet!!"
    return msg
    
@app.route('/state')
def hello_world():
    return 'Hello, World!'