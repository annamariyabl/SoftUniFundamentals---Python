efficiency1 = int(input())
efficiency2 = int(input())
efficiency3 = int(input())
students = int(input())
efficiency_hour = efficiency1 + efficiency2 + efficiency3
hours = 0
while students >= 0:
    if students == 0:
        print(f"Time needed: {hours}h.")
        break
    if hours % 4 == 0:
        hours+=1
        continue
    students = students - efficiency_hour
    if students <= 0:
        print(f"Time needed: {hours}h.")
        break
    hours += 1




