import pytest
import requests
import json


url = 'http://127.0.0.1:5000' # The root url of the flask app
locations= url+"/locations"

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
    }

def get_all_data():
    all_data = requests.get(locations)
    return all_data

def get_location_data(loc):
    loc_data = requests.get(locations+ "/"+loc)
    return loc_data

def verify_response(checkstring):
    all_inventory = get_all_data()
    assert all_inventory.status_code == 200
    assert checkstring in all_inventory.text

def test_get_index():
    r = requests.get(url+'/')
    assert r.status_code == 200

def test_hello_page():
    r = requests.get(url+'/greet')
    assert r.status_code == 200 
    assert "Hello from Server" in r.text

def test_get_locations():
    r= requests.get(url+'/locations')
    assert r.status_code == 200 

def test_post_first_loc():
    data = {
        'counter': ['calculator']
    }
    jdata=json.dumps(data)
    print(jdata)
    r = requests.post(url = url+'/locations',json=data)
    print(r.text)
    assert r.status_code == 201

def test_get_item1():
    checkfor = "calculator"
    verify_response(checkfor)

def test_add_items():
    data = {
        'counter': ['wallet', 'keys']
    }
    r = requests.post(url = url+'/locations',json=data)
    assert r.status_code == 201
    verify_response("wallet")
    verify_response("keys")






