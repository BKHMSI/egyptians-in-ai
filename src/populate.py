import json
import pandas as pd

def is_nan(string):
    return string != string

def read_json(file):
    with open(file, 'r', encoding='utf-8') as fin:
        data = json.load(fin)
    return data 

def write_json(file, data):
    with open(file, 'w', encoding="utf-8") as fout:
        json.dump(data, fout)

if __name__ == "__main__":

    out_file = "./assets/researchers_update.json"
    researchers = read_json('./assets/researchers.json')
    responses = pd.read_csv('./assets/researchers.csv', header=0)

    names = [entry["name"] for entry in researchers]

    for idx in range(len(responses)):
        response = responses.iloc[idx]
        name = response["Name"].strip()
        photo_link = response["Personal Photo Link"]
        scholar = response["Google Scholar Profile"].strip()
        linkedin = response["LinkedIn Profile"]
        twitter = response["Twitter Profile"]
        website = response["Personal Website"]
        interests = [interest.strip() for interest in response["Research Interests"].split(",")] if not pd.isna(response["Research Interests"]) else []
        if name not in names:
            researchers += [{
                "name": name,
                "affliation": response["Affiliation"].strip(),
                "position": response["Position"].strip(),
                "hindex": -1,
                "photo": photo_link if not is_nan(photo_link) else "./assets/images/default.jpg",
                "scholar": scholar,
                "linkedin": "" if is_nan(linkedin) else linkedin,
                "website": "" if is_nan(website) else website,
                "twitter": "" if is_nan(twitter) else twitter,
                "interests": interests
            }]
        
    write_json(out_file, researchers)
