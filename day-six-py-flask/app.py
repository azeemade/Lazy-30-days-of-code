from flask import Flask, request
import urllib.request
import json

app = Flask(__name__)

url = "http://jsonplaceholder.typicode.com/users"

response = urllib.request.urlopen(url)
data = response.read()
dict = json.loads(data)


def all():
    users = []
    for user in dict:
        users.append({
            'id': user['id'],
            'name': user['name'],
            'username': user['username'],
            'email': user['email']
        })

    return users


@app.route('/users', methods=['GET'])
def index():
    return all()


@app.route('/user/<string:query>', methods=['GET'])
def get(query):
    for user in all():
        if user['name'] == query:
            return user
        elif user['username'] == query:
            return user
        elif user['email'] == query:
            return user

    return "User not found"


@app.route('/user/delete', methods=['DELETE'])
def delete():
    users = all()
    users.pop(-1)
    return users


@app.route('/deleteall', methods=['DELETE'])
def deleteall():
    users = all()
    users.clear()
    return f'users deleted. users:{users}'


@app.route('/newuser', methods=['POST'])
def add():
    users = all()
    new_id = users[-1]["id"] + 1

    users.append({
        "id": new_id,
        "name": request.form['name'],
        "email": request.form['email'],
        "username": request.form['username']
    })
    return users
