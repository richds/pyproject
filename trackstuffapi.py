import simplejson as json
from flask import Flask, request, jsonify
from flask_restful import Api, reqparse, Resource

app = Flask(__name__)
containers = []

def importDatabase():
    global containers
    try:
        with open("apidata.txt") as file:
            if file.read(1):
                data = json.load(file)
            else:
                data = None
    except FileNotFoundError:
        open('apidata.txt', 'a').close()
        data = None

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

@app.route('/locations', methods=['GET','POST'])
def get_all_locations():
    locStuff = importDatabase()
    if locStuff == None:
        return "You don't have any locations.", 404
    if request.method == 'GET':
        outputLocations = []

        for i in range(0,len(locStuff)):
            outputLocations.append(locStuff[i])
        
        output = str(outputLocations)
        print(str(output))
        return output

    if request.method == 'POST':
        addLocation = []
        stringLoc=(request.get_data().decode('utf8'))
        addLocation.append(stringLoc)
        locStuff.append(addLocation)
        message = "Successfully added location "
        with open('data.txt', 'w') as outfile:
            json.dump(locStuff, outfile)
        return (message + stringLoc),201

@app.route('/locations/<loc>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def specific_locations():
    locStuff = importDatabase()
