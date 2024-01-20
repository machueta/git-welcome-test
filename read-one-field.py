import json
import requests

responce = requests.get("https://api.github.com/search/users?q=pentest")
json_data = responce.json()

print(json_data['total_count'])
print(json_data['items'][0]['html_url'])