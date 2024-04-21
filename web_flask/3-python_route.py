#!/usr/bin/python3
"""
starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
must use the option strict_slashes=False in your route definition
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route():
    """display Hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def route2():
    """display HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
