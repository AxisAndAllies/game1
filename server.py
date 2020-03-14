from flask import Flask
app = Flask(__name__)

@app.route('/state')
def hello_world():
    return 'Hello, World!'