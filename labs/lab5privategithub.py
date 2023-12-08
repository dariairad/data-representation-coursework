# Data Representation
# Lab 06.02: API Keys
# Part 2 - Get private data from GitHub

import requests
import json
from lab5config import config as cfg

filename = "lab6private.json"

url = 'https://api.github.com/repos/dariairad/privateone'

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))
repo_details = response.json()

print(f"Repository Name: {repo_details['name']}")
print(f"Description: {repo_details['description']}")
print(f"Default Branch: {repo_details['default_branch']}")
print(f"Private: {repo_details['private']}")
print(f"Watchers Count: {repo_details['watchers_count']}")
print("")


with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)