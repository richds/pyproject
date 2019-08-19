import simplejson as json
from flask import Flask, request, jsonify
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
