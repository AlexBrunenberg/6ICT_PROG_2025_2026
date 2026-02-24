""" Oefening 2 (   / 6): API -- CO2 uitstoot van websites 

API: https://api.websitecarbon.com/

Voorbeelden (CO2 uitstoot afgerond op 3 cijfers na de komma):
    Opgelet! De API geeft 2 soorten CO2 terug. Kies voor de optie 'grid'.

    Als jouw script dezelfde prints heeft als onderstaande voorbeelden,
    dan mag je ervanuit gaan dat het script correct gemaakt is.

    Website 1:
        Input || Welke website opzoeken: https://www.w3schools.com/
        Print || Deze website is 1578905 bytes groot, en veroorzaakt 0.397 gram CO2 uitstoot.
    Website 2:
        Input || Welke website opzoeken: https://github.com/
        Print || Deze website is 1948243 bytes groot, en veroorzaakt 0.490 gram CO2 uitstoot.
    Website 3:
        Input || Welke website opzoeken: abc
        Print || Geen geldige site opgegeven.

"""

import requests, json

url_extra = "https://www.w3schools.com/"

url = "https://api.websitecarbon.com/data" + url_extra

response = requests.get(url)
response_json = response.json()
if "error" in response_json:
    print("Geen geldige site opgegeven")
else:
    with open("6ICT_PROG_2025_2026/hfst_4 API/oefenmee/websitecarbon.json", "w") as fp:
        json.dump(response_json, fp)
        print("Data gedumpt!")
print(response_json)
# print(response_json['statistics']['co2']['grid']['grams'])
# print(f"Deze website is {response_json['bytes']} groot, en veroorzaakt {round(response_json['co2']['grid']['grams'], 3)} gram C02 uitstoot.")


