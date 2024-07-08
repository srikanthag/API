import requests
import random
import json
import string

from API_Test_Using_Python.Post_Request_API import post_request

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

#PUT Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("PUT url: " + url)
    headers = {"Authorization": auth_token}
    data = {
        "name": "Naveen Automation Labs",
        "email": generate_random_email(),
        "gender": "male",
        "status": "inactive"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Naveen Automation Labs"
    print(".......PUT/Update USER IS DONE.......")
    print(".......=====================.......")


#call
user_id = post_request()
put_request(user_id)