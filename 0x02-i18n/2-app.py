#!/usr/bin/env python3
""" creating a get locale babel func """

#  importing neccessary modules
from flask_babel import Babel
from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """config files with default settings """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    '''
        Render template for Babel usage.
    '''
    return render_template('2-index.html')



@babel.localeselector
def get_locale() -> str:
    '''
        Get user locale.
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
