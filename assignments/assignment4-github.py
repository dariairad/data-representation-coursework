from github import Github
from config import config as cfg # file containing access token
import requests

apikey = cfg["githubkey"]
g = Github(apikey)

old = "Andrew"
new = "Daria"

# Repository and file to be updated. Worked and tested on privateone depository created for lab
repo_name = "dariairad/privateone"  
file_path = "test.txt"  

# Function to retrieve file content and file information from the GitHub repository
def get_file(target_repo, target_file):
    repo = g.get_repo(target_repo)
    file_info = repo.get_contents(target_file)
    file_url = file_info.download_url
    response = requests.get(file_url)
    file_content = response.text
    return file_content, file_info

# Function to replace a string in the original content
def replace_string(original_content):
    new_content = original_content.replace(old, new)
    return new_content
 
# Function to update the content of a file in the GitHub repository
def update_repo(repo, file_info, new_content):
    gh_response = repo.update_file(file_info.path, "Textfile update", new_content, file_info.sha)
    return gh_response

original_content, file_info = get_file(repo_name, file_path)

new_content = replace_string(original_content)

repo = g.get_repo(repo_name)

# github_response = update_repo(repo, file_info, new_content)
# print(github_response)

update_repo(repo, file_info, new_content)