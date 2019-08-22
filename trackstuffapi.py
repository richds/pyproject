import json
import os
from flask import Flask, request, jsonify
from flask_restful import Api, reqparse, Resource

app = Flask(__name__)

def importDatabase():
    #data = {}
    try:
        with open("apidata.txt", "r") as file:
            #data = json.load(file)
            if os.stat("apidata.txt").st_size > 0:
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
  #  locStuff= {
   #     "desk":"paper",
    #    "chair":"pad",
     #   "splashscreen":"false"
    #} 
    #locStuff= importDatabase()
   # locStr= json.dumps(locStuff)
   # print("This is locStr: " +locStr)
    #locStuff= importDatabase()
    #with open('apidata.txt', 'w') as outfile:
     #       json.dump(locStuff, outfile)
    
    if request.method == 'GET':
        #outputLocations = {}

        #for i in range(0,len(locStuff)):
         #   outputLocations.append(locStuff[i])
        
        #output = str(outputLocations)
        #with open('apidata.txt', 'r') as file:
        #    locDict=json.load(file)
        locDict=importDatabase()
        if locDict == None:
            return "You don't have any locations.", 404
        locStr = jsonify(locDict)
        print("This is locStr: "+ str(locStr))
        return (locStr),200

    if request.method == 'POST':
        addLocation = {
            "grey": "foot",
            "melville": "whale"
        }
        currData=importDatabase()
        
        addData=request.get_json()
        currData.update(addData)
        message = "Successfully added location "
        with open('apidata.txt', 'w') as outfile:
            json.dump(currData, outfile)
        #return (message + stringLoc),201
        return (message),201

@app.route('/locations/<loc>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def specific_locations():
    locStuff = importDatabase()
