import os
import json
import time
import openai
import requests
import argparse
from tqdm import tqdm
from populate import read_json, write_json

MAX_ATTEMPTS = 10
API_KEY = os.getenv("OPENAI_API_SOCIAL")
API_ORG = "org-Jj29M8wPzNI1sLwXW3tuwhwI"
openai.organization = API_ORG
openai.api_key = API_KEY

def retry_request(url, payload, headers):
    for i in range(MAX_ATTEMPTS):
        try:
            response = requests.post(url, data=json.dumps(
                payload), headers=headers, timeout=90)
            json_response = json.loads(response.content)
            if "error" in json_response:
                print(json_response)
                print(f"> Sleeping for {2 ** i}")
                time.sleep(2 ** i) 
            else:
                return json_response
        except:
            print(f"> Sleeping for {2 ** i}")
            time.sleep(2 ** i)  # exponential back off
    raise TimeoutError()

def translate(prompt: str, model: str = 'gpt-3.5-turbo-0613'):
  
    url = "https://api.openai.com/v1/chat/completions"
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json', 'Authorization': f'Bearer {API_KEY}', 'OpenAI-Organization': API_ORG}

    print(f"> Translating using {model}")

    out_file = "./assets/researchers_ar_update.json"
    researchers = read_json("./assets/researchers.json")

    researchers_ar = []
    for researcher in tqdm(researchers):

        query = f"{prompt}\n{json.dumps(researcher)}"
        payload_data = {"role": "user", "content": f"{query}"}

        payload = {"messages": [payload_data], "model": model}
        response = retry_request(url, payload, headers)

        if "choices" in response:
            json_response = json.loads(response["choices"][0]["message"]["content"])
            researchers_ar += [json_response]
        else:
            print("> Error!")
            researchers_ar += [researcher]

        write_json(out_file, researchers_ar)
                    
if __name__ == "__main__":
   
    prompt = "Convert the following keys in the given JSON from English to Arabic: name, affiliation, position, interests. Keep the JSON in the same format and the keys in English:"
    translate(prompt)