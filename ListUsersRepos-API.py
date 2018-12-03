# Prints the name of every public Github repository owned by the specified username
# 
import requests

# *** CHANGE THIS FOR DIFFERENT USERNAME ***
username = "nwchinn"
# ******************************************

response = requests.get("https://api.github.com/users/" + username + r"/repos")
# Optional: Prints the status code of the response
# print("status code: ", response.status_code)

repos = response.json()
repo_names = []
for repo in repos:
	repo_names.append(repo["name"])

# Grabs name of Github User
response = requests.get("https://api.github.com/users/" + username)
data = response.json()
realname = data["name"]

print("Public Repositories for " + username + "(" + realname + "):")
print(repo_names)