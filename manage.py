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
def page_not_found():
    return "404 Page", 404


@app.errorhandler(500)
def internal_server_error():
    return "500 Page", 404


@app.route('/user', methods=['POST'])
def create_user():
    # 获得请求里的数据
    data = request.get_data()
    json_data = json.loads(data)
    name = json_data.get('name')
    age = json_data.get('age')
    # 创建新的用户
    user = User(name, age)
    users.append(user)
    user_id = user.id
    # 返回新的用户ID
    resp = make_response(json.dumps({"userID": user_id}), 200)

    print_users()
    return resp


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    # show the user profile for that user
    for user in users:
        if user.id == int(user_id):
            # 找到了
            resp = make_response(json.dumps({"name": user.name, "age": user.age}), 200)
            break
    else:
        # 没有找到
        resp = make_response(json.dumps({}), 404)

    print_users()
    return resp


@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    # 获得请求里的数据
    data = request.get_data()
    json_data = json.loads(data)
    name = json_data.get('name')
    age = json_data.get('age')
    for user in users:
        if user.id == int(user_id):
            user.name = name
            user.age = age
            # 找到了
            resp = make_response(json.dumps({}), 200)
            break
    else:
        # 没有找到
        resp = make_response(json.dumps({}), 404)

    print_users()
    return resp


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    for index, user in enumerate(users):
        if user.id == int(user_id):
            # 找到用户
            del users[index]
            resp = make_response(json.dumps({}), 200)
            break
    else:
        # 没有找到指定用户
        resp = make_response(json.dumps({}), 404)

    print_users()
    return resp


def print_users():
    print("-------- {0} users exist --------".format(len(users)))
    for user in users:
        print("user_id:{0}, user_name:{1}, user_age:{2}".format(user.id, user.name, user.age))

if __name__ == '__main__':
    # start application
    app.run(host='0.0.0.0', port=8080)
