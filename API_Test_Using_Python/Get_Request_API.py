import requests
import random
import json
import string


#base url:
base_url = "https://gorest.co.in"

#Auth token:
auth_token = "Bearer 7c5479079573074d7a5d32b7bce2515824e1f48eecd520d9b4067bb40a6f6556"

#get random email id:
def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

#GET Request
def get_request():
    url = base_url + "/public/v2/users"
    print("get url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......GET USER IS DONE.......")
    print(".......=====================.......")


#call
get_request()