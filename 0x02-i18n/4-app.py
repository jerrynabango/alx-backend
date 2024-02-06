#!/usr/bin/env python3
""" Force locale with URL parameter"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Request"""
    local = request.args.get("locale", '').strip()
    if local and local in Config.LANGUAGES:
        return local
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def basic_babel():
    """HTML rendering"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
