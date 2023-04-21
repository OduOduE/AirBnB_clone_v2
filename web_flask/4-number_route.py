#!/usr/bin/python3
""" starts a Flask web application: """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Print web """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Print web """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Print a char C and value of text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Print Python, followed by the value of the text variable,
    with default value of text: is cool """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ Number route """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)