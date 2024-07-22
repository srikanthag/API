import requests
import json
import jsonpath

Api_URL = "https://reqres.in/api/users"

file = open(r'C:\Users\hp\Desktop\IT\Testing\API_Test\JSOn_Files\create_user.json', 'r')
json_input = file.read()
requests_json = json.loads(json_input)
# print(requests_json)


# Make post in json body
response = requests.post(Api_URL, requests_json)
# print(response.content)
assert response.status_code  == 201


# Print header
# print(response.headers)

#parse response format
json_response = json.loads(response.text)
# print(json_response)


#json path
json_path = jsonpath.jsonpath(json_response, 'id')
print(json_path)














