# Gebruik onderstaande dictionary van dictionaries voor deze opdracht.
landinfo = {
    "belgie": {
        "provincie": {
            "naam": "limburg",
            "weetjes": {
                "oppervlakte":  2.422,
                "inwoners": 885.951,
                "gouverneur": "Jos Lantmeeters"
            }
        }
    }
}

print(landinfo["belgie"]["provincie"]["weetjes"]["gouverneur"])

landinfo["belgie"]["provincie"]["informatie"] = landinfo["belgie"]["provincie"]["weetjes"]

landinfo["belgie"]["provincie"].pop("weetjes")

print(landinfo)

inwoners = [
    ["mannen", "49.77%"], # Sleutel = mannen,  waarde = 49.77%
    ["vrouwen", "50.23%"] # Sleutel = vrouwen, waarde = 50.23%
]

landinfo["belgie"]["provincie"]["informatie"]["inwoners_gender"] = inwoners 

print(landinfo)