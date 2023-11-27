import re
new = []
text = input()
pattern = r"\b_([a-zA-Z0-9]+)\b"
matches = re.findall(pattern, text)
for match in matches:
    match_new = re.sub('_', "", match)
    new.append(match_new)

print(",".join(new))