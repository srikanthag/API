import requests
import json
import jsonpath

# Get requiest base url : https://reqres.in/api/users?page=2

Api_URL = "https://reqres.in/api/users?page=2"


# # Send get requests
response = requests.get(Api_URL)
print(response)

# # Display response content
print(response.content)
print(response.headers)

# Parse  response to JSON
JSON_Response = json.loads(response.text)
# print(JSON_Response)

#Fetch value using JSOn Path
pages = jsonpath.jsonpath(JSON_Response, 'total_pages')
# print(pages[0])
assert pages[0] == 2    # Asser will  compare
# assert pages[0] == 5    # user will get  assertion error












