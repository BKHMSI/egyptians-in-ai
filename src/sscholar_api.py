import json
import requests
from tqdm import tqdm
from dotmap import DotMap 

def write_json(path, data):
    with open(path, 'w') as fout:
        json.dump(data, fout)

def read_json(path):
    with open(path, 'r') as fin:
        data = json.load(fin)
    return data 

if __name__ == "__main__":

    researchers = read_json("./assets/researchers.json")

    api_request = "https://api.semanticscholar.org/graph/v1/author/search?query={}&fields=name,authorId,hIndex,homepage,affiliations,citationCount,paperCount&limit=5"

    data = {}
    for researcher in tqdm(researchers[:5]):
        name = researcher["name"]
        data[name] = [] 
        response = requests.get(api_request.format(researcher["name"]))
        if response.status_code != 200: 
            print(f"Error: {name}")
            continue 
        
        results = response.json()
        for res in results["data"]:
            res = DotMap(res)
            data[name] += [{
                "name": res.name,
                "authorId": res.authorId,
                "hIndex": res.hIndex,
                "homepage": res.homepage,
                "affiliations": res.affiliations,
                "citationCount": res.citationCount,
                "paperCount": res.paperCount
            }]
        data[name] = sorted(data[name], key=lambda x: x['hIndex'], reverse=True)    
    
    write_json("./sscholar_metadata.json", data)
        
