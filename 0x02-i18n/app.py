#!/usr/bin/env python3
"""Display the current time"""

import datetime
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from typing import Dict, Union


class Config(object):
    """Configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """User"""
    return users.get(int(id), None)


@babel.localeselector
def get_locale() -> str:
    """Request"""
    options = [
        request.args.get("locale", '').strip(),
        g.user.get("locale", None) if g.user else None,
        request.accept_languages.best_match(app.config["LANGUAGES"]),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale


@babel.timezoneselector
def get_timezone() -> str:
    """TimeZone"""
    t_zone = request.args.get("timezone", '').strip()
    if not t_zone and g.user:
        t_zone = g.user["timezone"]
    try:
        t_zone = pytz.timezone(t_zone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        t_zone = app.config["BABEL_DEFAULT_TIMEZONE"]
    return t_zone


@app.before_request
def before_request() -> None:
    """Request"""
    setattr(g, "user", get_user(request.args.get("login_as", 0)))
    setattr(g, "time", format_datetime(datetime.datetime.now()))


@app.route("/")
def basic():
    """HTML rendering"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()