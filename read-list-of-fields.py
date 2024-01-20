import json
import requests

responce = requests.get("https://api.github.com/search/users?q=pentest")
json_data = responce.json()
usersCount = len(json_data['items'])-1

for x in range(usersCount):
    print(json_data['items'][x]['html_url'])