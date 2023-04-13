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
    new_researchers = []

    names = [entry["name"] for entry in researchers]

    for idx in range(len(responses)):
        response = responses.iloc[idx]
        add_flag = response["Add or Update"] == "Add"

        if add_flag:
            name = response["Name"].strip()
            photo_link = response["Personal Photo Link"]
            scholar = str(response["Google Scholar Profile"]).strip()
            linkedin = response["LinkedIn Profile"]
            twitter = response["Twitter Profile"]
            website = response["Personal Website"]
            interests = [interest.strip() for interest in response["Research Interests"].split(",")] if not pd.isna(response["Research Interests"]) else []
            if name not in names:
                print(f"> [Add] {name}")
                new_researchers += [{
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
        else:
            name = response["Name.1"].strip()
            photo_link = response["Personal Photo Link.1"]
            scholar = str(response["Google Scholar Profile.1"]).strip()
            linkedin = response["LinkedIn Profile.1"]
            twitter = response["Twitter Profile.1"]
            website = response["Personal Website.1"]
            interests = [interest.strip() for interest in response["Research Interests.1"].split(",")] if not pd.isna(response["Research Interests.1"]) else []
            print(f"> [Update] {name}")
    write_json(out_file, new_researchers)
