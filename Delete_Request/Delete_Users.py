import requests


Api_URL = "https://reqres.in/api/users?page=2"

response = requests.delete(Api_URL)

# Fetch response
# print(response.status_code)

assert response.status_code == 204        # Asser will  compare
assert response.status_code == 200          # user will get  assertion error
