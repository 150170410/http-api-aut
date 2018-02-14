#!/usr/bin/env python
# coding=utf-8


class User(object):
    index = 0

    def __init__(self, name, age):
        User.index += 1
        self.id = User.index
        self.name = name
        self.age = age


if __name__ == "__main__":
    users = list()
    user = User("python", 1)
    users.append(user)
    user = User("python3", 3)
    users.append(user)

    for user in users:
        print(user.id, user.name, user.age)
