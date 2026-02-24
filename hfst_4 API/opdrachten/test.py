import requests, json
# response_json = requests.get(f"https://rickandmortyapi.com/api/location").json()
response_json = requests.get(f"https://pokeapi.co/api/v2/berry/1/").json()

with open("6ICT_PROG_2025_2026/hfst_4 API/opdrachten/test.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt")