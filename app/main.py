import json
import os
import types
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

@app.route('/locations', methods=['GET','POST','PUT','DELETE'])
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
            return "You don't have any locations.", 200
        locStr = jsonify(locDict)
        print("This is locStr: "+ str(locStr))
        return (locStr),200

    if request.method == 'POST':
        currData=importDatabase() #import current data from db
        if not currData:
                currData = {} #initialize currdata to avoid NPE later
        addData=request.get_json() #read in the POST data json, assign to addData
        newDictionary= {}
        for key in addData.keys(): #iterate over all the keys in current data
            
            if currData.get(key): #find out if the key exists in our current data
                newValues = currData[key] #pop out the key's data if it exists and assign values to newValues
                if type(newValues) is not list: #check if data is a list, otherwise make it one
                    newValues = [newValues]
                #if type(addData) is not list:
                #    newValues.append(addData[key]) #add the new value to the current data
                #else:
                for element in addData[key]:
                    newValues.append(element)
                
                newList = [element for element in currData[key] if element not in addData[key]]
                newValues = newList + addData[key]
                currData[key] = newValues
                newDictionary[key] = newValues 
            else:               
                currData[key] = addData[key]
                newDictionary[key] = addData[key]
        message = "Updated data: " + str(newDictionary)
        with open('apidata.txt', 'w') as outfile:
            json.dump(currData, outfile)
        #return (message + stringLoc),201
        return (message),201

    if request.method == 'PUT':
        currData=importDatabase()
        
        replaceData=request.get_json()

        currData.update(replaceData) # adds in new keys and overwrites existing key values with new data
        message = "Successfully changed current data. "
        with open('apidata.txt', 'w') as outfile:
            json.dump(currData, outfile)
        return (message),200

    if request.method == 'DELETE':
        currData=importDatabase() #import current data from db
        messageDict = {}
        removeData=request.get_json() #read in the DEL data json, assign to addData
        for key in removeData.keys(): 
            if not currData.get(key):
                return str(key) + "Not found", 404
            else:
                new_list = [element for element in currData[key] if element not in removeData[key]]
                currData[key] = new_list
                messageDict[key] = currData[key]
        message = "Location(s) updated to contain these items: " + str(messageDict)
        with open('apidata.txt', 'w') as outfile:
            json.dump(currData, outfile)
        return message, 200




@app.route('/locations/<location>', methods=['GET', 'DELETE'])
def alter_a_location(location):
    if request.method == 'GET':
        localDict = importDatabase()
        if localDict.get(location):
            data = localDict.get(location)
            return jsonify(data)
        else: 
            return "Not found", 404

    if request.method == 'DELETE':
        localDict = importDatabase()
        if localDict.get(location):
            toRemove = localDict.pop(location)
            with open('apidata.txt', 'w') as outfile:
                json.dump(localDict, outfile)
            return ("Removed "+ str(location) + " with items: " + str(toRemove)), 200
        else: 
            return "Not found", 404

#not implemented
    if request.method == 'PUT':
        addData=request.get_json()
        locationKey = get(addData)
        localDict = importDatabase()
        if localDict.get(location):
            origValues = localDict.get(location)
            if type(origValues) is not list:
                origValues = [origValues]
            
            print(str(addData))
            newValues = origValues.append(addData)
            localDict[location] = newValues
            with open('apidata.txt', 'w') as outfile:
                json.dump(localDict, outfile)
            return "OK", 201
        else:
            return "Not Found", 404


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = False
    app.run()