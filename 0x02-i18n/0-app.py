#!/usr/bin/env python3

from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


#  endpoint
@app.route('/', methods=['GET'], strict_slashes=False)
def helloWorld() -> str:
    """ returns a template """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
