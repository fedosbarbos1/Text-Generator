import json
import requests

# задание 1
url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
user_data = response.text

saved_data = json.loads(user_data)
data = saved_data["results"]
#print(data)

users_dict = {}
users_dict["users"] = data
def remove_n(users_dict):
    for k in users_dict.keys():
        if type(users_dict[k]) == str:
            users_dict[k] = users_dict[k].replace('\n', '')
        elif type (users_dict[k]) == dict:
            remove_n(users_dict[k])

remove_n(users_dict)

users_dict = json.dumps(users_dict, indent=4)
print(users_dict)