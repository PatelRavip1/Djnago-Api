from os import access
from traceback import print_tb
import requests


def getToken():
    url = "http://127.0.0.1:8000/api/token/refresh"

    payload = 'refresh=eyJ0eXAiOiJKV1Q90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MjQxMTk4NSwiaWF0IjoxNjQyMzI1NTg1LCJqdGkiOiI5MTFhNjlhMDE2ZWU0OTc0OWU5YzBmNThhOGE1Yzk0YSIsInVzZXJfaWQiOjF9.2YwgNIeVwH-g4oYKNb5i9xYpsMXYgigdnqy9Bbnr9fQ'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.json()
    return res["access"]
    # return response.text


getToken()
