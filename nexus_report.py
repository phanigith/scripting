import requests
import json
import sys

passw = "phani@557"

def help():
    print("""
    The way you executed the script is wrong.
    The script options are count, hosted, and proxy.
    Example to run the script is python3 nexus_report.py count
    """)
    sys.exit(130)

if len(sys.argv) < 2:
    help()

elif sys.argv[1] == "count":
    url = "http://3.83.55.98:8081/service/rest/v1/repositorySettings"
    response = requests.get(url, auth=('admin', passw))
    data = response.json()
    count = len(data)
    print(count)
    
elif sys.argv[1] == "hosted":
    url = "http://3.83.55.98:8081/service/rest/v1/repositorySettings"
    response = requests.get(url, auth=('admin', passw))
    data = response.json()
    hosted_repos = [repo['name'] for repo in data if repo['type'] == 'hosted']
    for repo in hosted_repos:
        print(repo)
    
elif sys.argv[1] == "proxy":
    url = "http://3.83.55.98:8081/service/rest/v1/repositorySettings"
    response = requests.get(url, auth=('admin', passw))
    data = response.json()
    proxy_repos = [(repo['name'], repo['url']) for repo in data if repo['type'] == 'proxy']
    for repo_name, repo_url in proxy_repos:
        print(repo_name + ", " + repo_url)
    
elif sys.argv[1] == "admin" and len(sys.argv) == 3 and sys.argv[2] == "mrc":
    print("PLEASE ENTER MAVEN REPO NAME")
    repo = input("Repo Name: ")
    with open('post.json', 'r') as file:
        json_data = file.read()
    json_data = json_data.replace('reponame', repo)
    url = "http://3.83.55.98:8081/service/rest/v1/repositories/maven/hosted"
    response = requests.post(url, auth=('admin', passw), data=json_data, headers={'Content-Type': 'application/json'})
    if response.status_code == 201:
        print("Repo creation successful")
    else:
        print("Repo creation failed")
else:
    help()
