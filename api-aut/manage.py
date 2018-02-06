#!/usr/bin/env python
# coding=utf-8
# start entry

import json
from flask import Flask
from flask import request, make_response
from user import User


app = Flask(__name__)
users = list()


@app.error_handlers(404)
def page_not_found(e):
    return "404 Page", 404


@app.error_handlers(500)
def page_not_found(e):
    return "500 Page", 404


@app.route('/user/<id>')
def show_user_profile(id):
    # show the user profile for that user
    if int(id) == 1:
        return 'admin'
    else:
        return 'others'


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_data()
    json_data = json.loads(data)
    name = json_data.get('name')
    age = json_data.get('age')
    print(name, age)





if __name__ == '__main__':
    # start application
    app.run(host='0.0.0.0', port=8080)