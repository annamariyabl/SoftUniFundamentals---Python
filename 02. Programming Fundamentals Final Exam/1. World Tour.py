stops = input()
command = input()
while command != "Travel":
    com = command.split(":")
    if 'Add Stop' in command:
        index = int(com[1])
        text = com[2]
        if index < len(stops):
            stops = stops[:(index)] + text + stops[(index):]
    elif "Remove" in command:
        com = command.split(":")
        start_index = int(com[1])
        end_index = int(com[2])
        if start_index >= 0 and end_index < len(stops):
            remove = stops[start_index:end_index+1]
            stops = stops.replace(remove, "")
    elif 'Switch' in command:
        old_string = com[1]
        new_string = com[2]
        stops = stops.replace(old_string, new_string)
    print(stops)
    command = input()
print(f'Ready for world tour! Planned stops: {stops}')




