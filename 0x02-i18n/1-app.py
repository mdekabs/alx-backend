#!/usr/bin/env python3
"""
    Basic Babel setup.
"""

#  Importing neccessary modules
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """ config file """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


#  endpoint
@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    '''
        Render template for Babel usage.
    '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
