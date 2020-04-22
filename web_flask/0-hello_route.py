#!/usr/bin/python3
""" Script that starts the flask connection """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'

app.run(host='0.0.0.0', port=5000)
