import requests
import json
import jsonpath

Api_URL = "https://reqres.in/api/users/2"

file = open(r'C:\Users\hp\Desktop\IT\Testing\API_Test\JSOn_Files\create_user.json', 'r')
json_input = file.read()
requests_json = json.loads(json_input)
# print(requests_json)


# Make put in json body
response = requests.put(Api_URL, requests_json)
# print(response.content)
assert response.status_code  == 200

#parse response format
json_response = json.loads(response.text)
print(json_response)


