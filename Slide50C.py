#Write a program that contains a list of grades. The program will print how many students passed the exam (a grade of 70 and above).
grades = [80, 90, 70, 60, 95, 55, 88, 92, 30, 82, 91, 87, 89, 94, 83, 86, 90, 80, 84]
passed = 0
for grade in grades:
    if grade >= 70:
        passed += 1
print("Number of students who passed:", passed) 