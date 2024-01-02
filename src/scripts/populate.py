import json
import numpy as np
import pandas as pd
from datetime import datetime

def is_nan(string):
    return string != string

def read_json(file):
    with open(file, 'r', encoding='utf-8') as fin:
        data = json.load(fin)
    return data 

def write_json(file, data):
    with open(file, 'w', encoding="utf-8") as fout:
        json.dump(data, fout, ensure_ascii=False)

if __name__ == "__main__":

    out_new_file = "./assets/researchers_new.json"
    out_update_file = "./assets/researchers_update.json"

    researchers = read_json('./assets/researchers_en.json')
    responses = pd.read_csv('./assets/researchers.csv', header=0)

    new_researchers = []
    to_update_researchers = []

    last_update = datetime.strptime("8/30/2023", "%m/%d/%Y")

    names = [entry["name"] for entry in researchers]

    for idx in range(len(responses)):
        response = responses.iloc[idx]
        add_flag = response["Add or Update"] == "Add"
        timestamp = datetime.strptime(response["Timestamp"], "%m/%d/%Y %H:%M:%S")
        if timestamp < last_update:
            continue
        
        if add_flag and not pd.isna(response["Name"]):
            name = response["Name"].strip()
            photo_link = response["Personal Photo Link"]
            scholar = str(response["Google Scholar Profile Link"]).strip()
            linkedin = response["LinkedIn Profile"]
            twitter = response["Twitter Profile"]
            website = response["Personal Website"]
            interests = [interest.strip() for interest in response["Research Interests"].split(",")] if not pd.isna(response["Research Interests"]) else []
            if name not in names:
                print(f"> [Add] {name}")
                new_researchers += [{
                    "name": name,
                    "affiliation": response["Affiliation"].strip(),
                    "position": response["Position"].strip(),
                    "hindex": -1,
                    "photo": photo_link if not is_nan(photo_link) else "./assets/images/default.jpg",
                    "scholar": scholar,
                    "linkedin": "" if is_nan(linkedin) else linkedin,
                    "website": "" if is_nan(website) else website,
                    "twitter": "" if is_nan(twitter) else twitter,
                    "interests": interests,
                    "citedby": 0,
                    "lastupdate": ""
                }]
        elif not pd.isna(response["Name.1"]):
            name = response["Name.1"].strip()
            photo_link = response["Personal Photo Link.1"]
            scholar = str(response["Google Scholar Profile"]).strip()
            linkedin = response["LinkedIn Profile.1"]
            twitter = response["Twitter Profile.1"]
            website = response["Personal Website.1"]
            interests = [interest.strip() for interest in response["Research Interests.1"].split(",")] if not pd.isna(response["Research Interests.1"]) else []
            print(f"> [Update] {name}")
            to_update_researchers += [{
                    "name": name,
                    "affiliation": response["Affiliation.1"].strip(),
                    "position": response["Position.1"].strip(),
                    "hindex": -1,
                    "photo": photo_link if not is_nan(photo_link) else "./assets/images/default.jpg",
                    "scholar": scholar,
                    "linkedin": "" if is_nan(linkedin) else linkedin,
                    "website": "" if is_nan(website) else website,
                    "twitter": "" if is_nan(twitter) else twitter,
                    "interests": interests,
                    "citedby": 0,
                    "lastupdate": ""
                }]
            
    write_json(out_new_file, new_researchers)
    write_json(out_update_file, to_update_researchers)
