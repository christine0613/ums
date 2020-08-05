import pytest
from ums import Users
from ums import app as flask_app
import json
import responses
import requests


def test_if_homepage_loads(app, client):
    res = client.get('http://127.0.0.1:5001/')
    assert res.status_code == 200
    
def test_if_add_user_succeed(app, client):
    resp = requests.post('http://127.0.0.1:5001/add_user', form={"addFirstName":"Minh", "addLastName":"Nguyen", "addEmail":'a@gmail.com', "addDob" :4324234})
    assert res.status_code == 200

def 