import json

import requests


def getAPIData(url, params=None, OpHeader=None):
    response = requests.get(url, verify=False, headers=OpHeader, params=params)
    print("Requests URL: " + url)
    print("request header", response.request.headers)
    print("response header", response.headers)
    return response


def postAPIData(url, body):
    headers = {'Content-type': 'application/json'}
    print("\nReqURL:" + url)
    print("ReqBody:" + json.dumps(body))  # converts json to dict
    return requests.post(url, verify=False, json=body, headers=headers)
