# Vul groene vakken in OneNote aan.

# import requests, json

# url = "https://api.themoviedb.org/3/movie/18?language=en-US"
# response = requests.get(url)
# response_json = response.json()

# print(response_json)

import requests

url = "https://api.themoviedb.org/3/movie/18?language=en-US"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)