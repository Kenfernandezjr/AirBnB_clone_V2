#!/usr/bin/python3
""" Script that starts the flask connection """

from flask import Flask, render_template
app = Flask(__name__,
            template_folder="templates")
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is_cool(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def numbers(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def templates(n):
    return render_template('5-number.html',
                           n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html',
                           n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
