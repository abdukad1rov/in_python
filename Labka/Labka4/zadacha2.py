
def sort_students(students):
    return sorted(students, key=lambda x: x[1])

students = []
while True:
    student = input("Enter a student (name class) or type '0' to stop: ").strip()
    if student.lower() == "0":
        break
    name,class_ = student.split()
    students.append((name, int(class_)))

sorted_students = sort_students(students)

for name, class_ in sorted_students:
    print(f"{name} {class_}")

print(sorted_students)
