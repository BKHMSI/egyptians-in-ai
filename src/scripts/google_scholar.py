import re
import json 
import time
import datetime
from tqdm import tqdm 
from scholarly import scholarly

def write_json(path, data):
    with open(path, 'w') as fout:
        json.dump(data, fout)

def read_json(path):
    with open(path, 'r') as fin:
        data = json.load(fin)
    return data 

if __name__ == "__main__":

    out_file = "./assets/researchers_update_3.json"
    # 57, 105, 106
    researchers = read_json("./assets/researchers_en.json")[107:]

    timestamp = time.time()
    # Convert the timestamp to a datetime object
    datetime_obj = datetime.datetime.fromtimestamp(timestamp)
    # Format the datetime object into a readable date format
    formatted_date = datetime_obj.strftime("%Y-%m-%d")

    for researcher in tqdm(researchers):
        scholar_link = researcher["scholar"]
        pattern = r'user=([\w-]+)'
        match = re.search(pattern, scholar_link)
        if match:
            scholar_id = match.group(1)
            author = scholarly.fill(scholarly.search_author_id(scholar_id))
            if author["hindex"] != researcher["hindex"]:
                print(f"Updating {researcher['name']} h-index: {researcher['hindex']} --> {author['hindex']}") 
            researcher["hindex"] = author['hindex']
            researcher["citedby"] = author["citedby"]
            researcher["lastupdate"] = formatted_date
        else:
            if "lastupdate" not in researcher:
                researcher["lastupdate"] = ""
                researcher["citedby"] = 0
            print(f"{researcher['name']} not found!")
    
        write_json(out_file, researchers)
