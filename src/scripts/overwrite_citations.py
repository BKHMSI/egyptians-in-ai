import json 
from gscholar import read_json

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as fout:
        json.dump(data, fout, ensure_ascii=False)

if __name__ == "__main__":

    data_en = read_json("./assets/researchers_en.json")
    data_ar = read_json("./assets/researchers_ar.json")

    for i, row in enumerate(data_en):
        if data_ar[i]["photo"] != row["photo"]:
            print(f"> Updating Photo: {row['photo']}")
            data_ar[i]["photo"] = row["photo"]
            
        data_ar[i]["citedby"] = row["citedby"]
        data_ar[i]["lastupdate"] = row["lastupdate"]

    write_json("./assets/researchers_ar.json", data_ar)

    