#!/usr/bin/python3
"""Starts a Flask web application... """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Print 'Hello HBNB!' on web """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """Displays 'C' followed by the value of <text>
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """Displays 'Python' followed by the value of <text>
    Replaces any underscores in <text> with slashes.
    """
    return 'Python {}'.format(text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    """Displays 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000)
