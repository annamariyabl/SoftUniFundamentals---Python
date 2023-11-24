import re

dates = input()
regex = "\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b"
matches = re.finditer(regex,dates)
for match in matches:
    print(f"Day: {match[1]}, Month: {match[3]}, Year: {match[4]}")
