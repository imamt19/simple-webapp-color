import os
from flask import Flask
from flask import render_template
import socket
import random
import os

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(["red","green","blue","blue2","darkblue","pink"])

@app.route("/")
def main():
    print(color)
    return render_template('hello.html', name="Imam Tajuddin", color=color_codes[color])  # <--- diubah di sini

@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name="Imam Tajuddin", color=color_codes[new_color])  # <--- di sini juga

@app.route('/read_file')
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return render_template('hello.html', name="Imam Tajuddin", contents=contents, color=color_codes[color])  # <--- dan ini

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

