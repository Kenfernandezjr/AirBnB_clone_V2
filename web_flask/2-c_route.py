#!/usr/bin/python3
""" Script that starts the flask connection """

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_is(txt):
    txt = txt.replace("_", " ")
    return "C {}".format(txt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)