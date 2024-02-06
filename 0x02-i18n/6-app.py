#!/usr/bin/env python3
"""Use user locale"""

from flask import Flask, render_template, request, g
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
    local = request.args.get('locale')
    if local in app.config["LANGUAGE"]:
        return local
    if g.user:
        local = g.user.get("locale")
        if local and local in app.config["LANGUAGES"]:
            return local
    local = request.headers.get("locale", None)
    if local in app.config["LANGUAGES"]:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """User"""
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """Request"""
    user = get_user()
    g.user = user


@app.route("/")
def basic_babel():
    """HTML rendering"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
