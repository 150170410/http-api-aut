#!/usr/bin/env python
# coding=utf-8
# start entry

from flask import Flask

app = Flask(__name__)


@app.route('/user/<id>')
def show_user_profile(id):
    # show the user profile for that user
    if int(id) == 1:
        return 'admin'
    else:
        return 'others'


if __name__ == '__main__':
    # start application
    app.run(host='0.0.0.0', port=2222)