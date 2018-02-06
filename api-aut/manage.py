#!/usr/bin/env python
# coding=utf-8
# start entry

import json
from flask import Flask
from flask import request, make_response
from user import User


app = Flask(__name__)
users = list()


@app.errorhandler(404)
def page_not_found(e):
    return "404 Page", 404


@app.errorhandler(500)
def internal_server_error(e):
    return "500 Page", 404


@app.route('/user/<user_id>', methods=['GET'])
def show_user_profile(user_id):
    # show the user profile for that user
    for user in users:
        if user.id == int(user_id):
            break
    resp = make_response(json.dumps({"name": user.name, "age": user.age}), 200)
    return resp


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_data()
    json_data = json.loads(data)
    name = json_data.get('name')
    age = json_data.get('age')
    user = User(name, age)
    users.append(user)
    user_id = user.id
    print(name, age)
    resp = make_response(json.dumps({"userID": user_id}), 200)
    return resp





if __name__ == '__main__':
    # start application
    app.run(host='0.0.0.0', port=8080)