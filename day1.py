name = input("Enter name: ")

marks = []
for i in range(3):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
percentage = total / 3

if percentage >= 90:
    grade = "A"
elif percentage >= 50:
    grade = "Pass"
else:
    grade = "Fail"

print("\nName:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
