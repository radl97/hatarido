#!/usr/bin/env python3

from flask import Flask, render_template, request
from model import load_model, weekdays

app = Flask(__name__, static_url_path="/")

@app.route('/', methods=["GET"])
def main_page():
    return render_template("index.html", days=load_model(), weekdays=weekdays())

if __name__ == "__main__":
    app.run(port=5000)
