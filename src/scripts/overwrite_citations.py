import os 
from gscholar import read_json, write_json


if __name__ == "__main__":

    data_en = read_json("./assets/researchers_en.json")
    data_ar = read_json("./assets/researchers_ar.json")

    for i, row in enumerate(data_en):
        assert data_ar[i]["photo"] == row["photo"]
        data_ar[i]["citedby"] = row["citedby"]
        data_ar[i]["lastupdate"] = row["lastupdate"]

    write_json("./assets/researchers_ar.json", data_ar)

    