n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    m = int(input())
    marks.append(m)

valid_students = 0
failed_students = 0

for mark in marks:

    if mark < 0 or mark > 100:
        category = "Invalid"

    else:
        valid_students += 1

        if 90 <= mark <= 100:
            category = "Excellent"

        elif 75 <= mark <= 89:
            category = "Very Good"

        elif 60 <= mark <= 74:
            category = "Good"

        elif 40 <= mark <= 59:
            category = "Average"

        else:
            category = "Fail"
            failed_students += 1

    print(mark, "->", category)

print("Total Valid Students:", valid_students)
print("Total Failed Students:", failed_students)
