import requests
import random
import json
import string

from API_Test_Using_Python.Post_Request_API import post_request
from API_Test_Using_Python.Put_Request_API import put_request

#base url:
base_url = "https://gorest.co.in"

#Auth token:
auth_token = "Bearer <TokenID>"

#get random email id:
def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

#DELETE Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print(".......DELETE USER IS DONE.......")
    print(".......=====================.......")


#call
# user_id = post_request()
# put_request(user_id)
delete_request()