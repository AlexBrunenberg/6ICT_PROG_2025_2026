# Start de oefen mee met onderstaande dictionary.
planner = {
    "Slaap": 8,
    "Werk":  8,
    "Ontspanning": 8
}
print("planning voor morgen")
tijd_over = 24
for onderdeel, tijd in planner.items():
    print(f" - {onderdeel}:{tijd} u")
    tijd_over = tijd_over - tijd
print(f"Je hebt {tijd_over} u over.")