import math

students_number = int(input())
lectures = int(input())
bonus = int(input())
max = 0
att = 0
for i in range(students_number):
    attendance = int(input())
    total_bonus = attendance / lectures *(5 + bonus)
    total_bonus = math.ceil(total_bonus)
    if total_bonus >= max:
        max = total_bonus
        att = attendance

print(f"Max Bonus: {max}.")
print(f"The student has attended {att} lectures.")

