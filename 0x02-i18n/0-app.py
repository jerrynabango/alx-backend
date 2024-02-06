#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template
from flask import app


@app.route("/")
def basic():
    return render_template("index.html")
