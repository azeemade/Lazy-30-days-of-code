from flask import Flask, render_template, request, url_for, redirect, jsonify
from pymongo import MongoClient
import urllib.request
import json
from bson import json_util

app = Flask(__name__)

client = MongoClient('127.0.0.1', 27017)

db = client.flask_db
users = db.users

url = "http://jsonplaceholder.typicode.com/users"

response = urllib.request.urlopen(url)
data = response.read()
dict = json.loads(data)


@app.route('/populate', methods=['GET'])
def populate():
    users.insert_many([
        {
            'name': user['name'],
            'username': user['username'],
            'email': user['email']
        } for user in dict])


@app.route('/users', methods=['GET'])
def index():
    return json.loads(json_util.dumps(users.find()))


@app.route('/user/<string:query>', methods=['GET'])
def get(query):
    for user in users.find():
        if user['name'] == query:
            return json.loads(json_util.dumps(user))
        elif user['username'] == query:
            return json.loads(json_util.dumps(user))
        elif user['email'] == query:
            return json.loads(json_util.dumps(user))

    return "User not found"


@app.route('/user/delete', methods=['DELETE'])
def delete():
    allUsers =  users.find()
    size =  users.estimated_document_count()
    last = allUsers[size-1]
    result = users.delete_one(last)

    return json.loads(json_util.dumps([{
        "message": "Last user deleted.",
        "users": allUsers
    }]))


@app.route('/deleteall', methods=['DELETE'])
def deleteall():
    for user in users.find():
        users.delete_one(user)

    return json.loads(json_util.dumps([{
        "message": "users deleted.",
        "users": users.find()
    }]))


@app.route('/newuser', methods=['POST'])
def add():
    users.insert_one({
        "name": request.form['name'],
        "email": request.form['email'],
        "username": request.form['username']
    })

    return json.loads(json_util.dumps([{
        "message": "new user added",
        "users": users.find()
    }]))