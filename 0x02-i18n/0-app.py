#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def basic() -> str:
    """HTML rendering"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
