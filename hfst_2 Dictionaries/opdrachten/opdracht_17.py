# Maak de opdracht met behulp van onderstaande dictionary.
ranglijst_voedsels = {
    "A": ["water"],
    "B": ["groenten", "fruit", "soja", "granen"],
    "C": ["vis", "gevogelte", "kaas", "zuivel"],
}

for sleutel, waarde in ranglijst_voedsels.items():
    print(f"Eten van rang {sleutel}:")
    for index in range(len(waarde)):
        print(f"-{waarde[index]}")