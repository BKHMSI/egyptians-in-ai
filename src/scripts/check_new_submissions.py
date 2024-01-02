import re
import json 
import time
import datetime
from tqdm import tqdm 
from scholarly import scholarly

HINDEX_THRESH = 5

def write_json(path, data):
    with open(path, 'w') as fout:
        json.dump(data, fout)

def read_json(path):
    with open(path, 'r') as fin:
        data = json.load(fin)
    return data 

if __name__ == "__main__":

    out_file = "./assets/researchers_new.json"
    researchers = read_json("./assets/researchers.json")
    new_researchers = []

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
            breakpoint()
            researcher["hindex"] = author['hindex']
            researcher["citedby"] = author["citedby"]
            researcher["lastupdate"] = formatted_date
            if author["hindex"] >= HINDEX_THRESH:
                print(f"Adding {researcher['name']} | h-index: {researcher['hindex']}")
                new_researchers += [researcher]
            else:
                print(f"Skipping {researcher['name']} | h-index: {researcher['hindex']}")
        else:
            print(f"{researcher['name']} not found!")
    
    write_json(out_file, new_researchers)