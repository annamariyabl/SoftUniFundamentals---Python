import re
places = input()
pattern = r"([=/])([A-Z][A-Za-z]{2,})(\1)"
valid_places = re.findall(pattern, places)
places = []
travel_points =0
for i in valid_places:
    places.append(i[1])
    travel_points += len(i[1])
print(f"Destinations: {', '.join(places)}")
print(f"Travel Points: {travel_points}")
