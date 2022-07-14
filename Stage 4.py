import json
import requests
import pandas as pd
import re
import numpy as np

url = "https://randomuser.me/api/?results=1000"
my_params = {"inc": ["gender, email, phone"]}
response1 = requests.get(url, params=my_params)
user_data1 = response1.text

saved_data1 = json.loads(user_data1)
data1 = saved_data1["results"]
#print(data1)

DF = pd.DataFrame(data1)
#print(DF)

DF["name"] = DF["email"].apply(lambda name: name.capitalize())

def includes_words(name):
    inc_name = name.find("@")
    if inc_name == -1:
        return inc_name
    else:
        return name[:inc_name + 0]

def get_name(name):
    name = includes_words(name)
    name_list = name.split(".")
    name = name_list[0]
    return name

def get_surname(name):
    name = includes_words(name)
    name_list = name.split(".")
    surname = name_list[1]
    return surname.capitalize()

DF["name"] = DF["name"].apply(get_name)
DF["surname"] = DF["surname"].apply(get_surname)

#print(DF)

DF_gender = DF[DF["gender"] == "female"]
DF_gender.to_csv("female.csv", sep=",", index=False, encoding="utf-8")