import json
from flask import Flask
from flask_restful import Api, reqparse, Resource

app = Flask(__name__)
containers = []

def importDatabase():
    global containers
    with open("data.txt") as file:
        data = json.load(file)
    if data == None:
        return "You don't currently have any stuff tracked"
    else:
        print("This is your data: " + str(data))
        return data

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/stuff')
def allstuff():
    yourStuff = str(importDatabase())
    return yourStuff



