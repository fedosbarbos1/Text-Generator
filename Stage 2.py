import json
import requests
import pandas as pd


url = "https://randomuser.me/api/?results=1000"
my_params = {"inc": ["gender, email, phone"]}
response1 = requests.get(url, params=my_params)
user_data1 = response1.text

saved_data1 = json.loads(user_data1)
data1 = saved_data1["results"]
#print(data1)

DF = pd.DataFrame(data1)
print(DF)