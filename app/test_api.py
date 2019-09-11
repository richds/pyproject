import pytest
import requests
import json


url = 'http://host.docker.internal:80' # The root url of the flask app
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

def post_new_data(newstuff):
    r = requests.post(url = url+'/locations',json=newstuff)
    assert r.status_code == 201

def put_data(newdata):
    r = requests.put(url = url+'/locations',json=newdata)
    assert r.status_code == 200

def verify_get_data(checkstring=[]): #input can be a string or list of strings
    all_inventory = get_all_data()
    
    assert all_inventory.status_code == 200
    if not isinstance(checkstring, list):
        checkstring = [checkstring]
    for x in checkstring:
        print("Checking for this item: "+ str(x))
        assert x in all_inventory.text

def verify_get_a_location(checkloc,checkstring=[]):
    all_inventory = get_location_data(checkloc)
    assert all_inventory.status_code == 200
    if not isinstance(checkstring, list):
        checkstring = [checkstring]
    for x in checkstring:
        print("Checking for this item: "+ str(x))
        assert x in all_inventory.text


def verify_does_not_contain(checkstring=[]):
    all_inventory = get_all_data()
    if not isinstance(checkstring, list):
        checkstring = [checkstring]
    for x in checkstring:
        print("Checking this item is gone: "+ str(x))
        assert x not in all_inventory.text
    

def test_get_index():
    r = requests.get(url+'/')
    print("base url is: " + r.url)
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
    verify_get_data(checkfor)

def test_add_items():
    data = {
        'counter': ['wallet', 'keys']
    }
    r = requests.post(url = url+'/locations',json=data)
    assert r.status_code == 201
    verify_get_data("wallet")
    verify_get_data("keys")

def test_add_multiple():
    data = {
        'counter': ['glasses'],
        'desk': ['cup', 'picture', 'coaster']
    }
    post_new_data(data)
    verify_get_data(['glasses', 'cup', 'picture', 'coaster'])
    verify_get_data(["counter","desk"])

def test_change_inventory():
    data = {
        'backpack': ['map', 'headphones'],
        'desk': ['picture','card','papers']
    }
    put_data(data)
    verify_get_data(['map','headphones','backpack','desk','picture','card','papers'])
    verify_does_not_contain(['cup','coaster'])

@pytest.mark.parametrize("location, expected_values", 
    [("backpack",'map'),
    ('desk','picture')]
)
def test_get_location(location, expected_values):
    verify_get_a_location(location, expected_values)

def test_remove_item():
    data = {
        'counter': ['keys', 'glasses'],
        'backpack': ['headphones']
    }
    r = requests.delete(url = url+'/locations', json = data)
    assert r.status_code == 200
    assert 'Location(s) updated' in r.text 
    verify_does_not_contain(['keys', 'glasses', 'headphones'])
    verify_get_data(['counter', 'backpack'])


def test_delete_location():
    to_be_deleted="desk"
    r = requests.delete(url = url+'/locations/'+to_be_deleted)
    assert r.status_code == 200
    assert "Removed desk" in r.text
    r = requests.get(url = url+'/locations/'+to_be_deleted)
    r.status_code = 404

def test_final_state():
    verify_get_data(['map', 'calculator', 'wallet'])





