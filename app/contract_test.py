import atexit
import pytest
import requests
from pactman import Consumer, Provider

#from pact import Consumer, Provider
 
#pact = Consumer('buildReader').has_pact_with(Provider('bringon'))

#pact.start_service()
#atexit.register(pact.stop_service)

pact = Consumer('Consumer').has_pact_with(Provider('Provider'), version='3.0.0')

def test_interaction():
    pact.given("some data exists").upon_receiving("a request") \
        .with_request("get", "/", query={"foo": ["bar"]}).will_respond_with(200)
    with pact:
        requests.get(pact.uri, params={"foo": ["bar"]})

def test_server_is_up():
    pact.given("The Server is online").upon_receiving("a request") \
        .with_request("get", "/", headers={'Content-Type': 'application/json'}) \
            .will_respond_with(200, body= 'Server Works!', headers={'Content-Type': 'application/json'})
    with pact:
        r = requests.get(pact.uri, headers={'Content-Type': 'application/json'})
        print (r.text)
    