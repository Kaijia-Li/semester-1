# Worksheet 1.2: Task 1 Solution
grade = int(input("please input you score"))

if grade < 0 or grade > 100:
    print("Error: Grade must be an integer between 0 and 100")

if grade >= 70:
    result = "Distinction"
elif grade >= 40:
    result = "Pass"
else:
    result = "Fail"

print(f"{grade} is a {result}")