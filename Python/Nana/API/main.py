import requests

my_projects = requests.get("https://api.github.com/users/juronja/repos").json()

print(my_projects[0])

for element in my_projects:
    print(f"Project name: {element["name"]}, url: {element["url"]}")