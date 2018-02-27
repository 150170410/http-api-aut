#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# main script

import json
from flask import Flask
from flask import request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# mysql user=root, password = 123456
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:123456@localhost/api'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'  # 绑定表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    age = db.Column(db.Integer, unique=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<User %r, %r, %r>' % (self.id, self.name, self.age)

    @staticmethod
    def show():
        users = User.query.all()
        for user in users:
            print(user)


@app.errorhandler(404)
def page_not_found():
    return "404 Page", 404


@app.errorhandler(500)
def internal_server_error():
    return "500 Page", 500


@app.route('/user', methods=['POST'])
def create_user():
    # 获得请求里的数据
    data = request.get_data()
    json_data = json.loads(data)
    name = json_data.get('name')
    age = json_data.get('age')
    # 创建新的用户
    user = User(name, age)
    db.session.add(user)
    db.session.commit()

    User.show()     # print for debugging
    user_id = user.id
    # 返回新的用户ID
    resp = make_response(json.dumps({"userID": user_id}), 200)
    return resp


@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    users = User.query.all()

    # show the user profile for that user
    for user in users:
        if user.id == int(user_id):
            # 找到了
            resp = make_response(json.dumps({"name": user.name, "age": user.age}), 200)
            break
    else:
        # 没有找到
        resp = make_response(json.dumps({}), 404)

    User.show()     # print for debugging
    return resp


@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    # 获得请求里的数据
    data = request.get_data()
    json_data = json.loads(data)
    name = json_data.get('name')
    age = json_data.get('age')
    users = User.query.all()
    for user in users:
        if user.id == int(user_id):
            user.name = name
            user.age = age
            db.session.add(user)
            db.session.commit()
            # 找到了
            resp = make_response(json.dumps({}), 200)
            break
    else:
        # 没有找到
        resp = make_response(json.dumps({}), 404)
    User.show()     # print for debugging
    return resp


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = User.query.all()
    for user in users:
        if user.id == int(user_id):
            # 找到用户
            db.session.delete(user)
            db.session.commit()
            resp = make_response(json.dumps({}), 200)
            break
    else:
        # 没有找到指定用户
        resp = make_response(json.dumps({}), 404)

    User.show()     # print for debugging
    return resp


if __name__ == '__main__':
    # start application
    app.run(host='0.0.0.0', port=8080)
