from github import Github
from config import config as cfg
import requests

apikey = cfg["githubkey"]
g = Github(apikey)

old = "Andrew"
new = "Daria"

# Repository and file to be updated
repo_name = "dariairad/privateone"  
file_path = "test.txt"  

# Function to retrieve file content and file information from the GitHub repository
def get_file(target_repo, target_file):
    repo = g.get_repo(target_repo)
    file_info = repo.get_contents(target_file)
    url_file = file_info.download_url
    response = requests.get(url_file)
    content_file = response.text
    return content_file, file_info

# Function to replace a string in the original content
def replace_string(original_content):
    new_content = original_content.replace(old, new)
    return new_content
 
# Function to update the content of a file in the GitHub repository
def update_github(repo, file_info, new_content):
    gitHubResponse = repo.update_file(file_info.path, "Textfile update", new_content, file_info.sha)
    return gitHubResponse

original_content, file_info = get_file(repo_name, file_path)

new_content = replace_string(original_content)

repo = g.get_repo(repo_name)

git_response = update_github(repo, file_info, new_content)

print(git_response)
