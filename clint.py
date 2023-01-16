import requests
import getToken
url = "http://127.0.0.1:8000"

payload = {}
token = getToken.getToken()
print('here')
headers = {
    # eyJ0eXAiOiJKV1QiLCJhbNjZXNzIiwiZXhwIjoxNjQyMzQ2NzAwLCJpYXQiOjE2NDIzMjU1ODUsImp0aSI6Ijg2MTE1OTJhNGMxMDQzNTI4MDZhM2U2M2NkNzU3NmNkIiwidXNlcl9pZCI6MX0.dntYjkgAhZZ_DdxOLZq9NSPtBK4ZNU38ogh-JrJ7pXQ'
    'Authorization': 'Bearer {}'.format(token)
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
