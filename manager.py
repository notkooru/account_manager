import json


class User:
    def __init__(self, username, password, description) -> None:
        self.username = username
        self.password = password
        self.description = description


users = []


def create_user():
    pass

def read_users():
    pass

def update_user():
    pass

def delete_user():
    pass


def save_database():
    global users
    db = json.dumps(users, indent=4)
    f = open("database.txt", "w")
    f.write(db)
    f.close()

def load_database():
    global users
    f = open("database.txt", "r")
    users = json.loads(f.read())
    f.close()