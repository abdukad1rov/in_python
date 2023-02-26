students = []

# ввод данных учащихся
while True:
    name = input("Введите имя учащегося (или '0' для завершения ввода): ")
    if name == "0":
        break
    group = input("Введите название группы: ")
    section = input("Введите название секции: ")
    students.append({"name": name, "group": group, "section": section})

# упорядочивание списка по категориям
by_group = {}
by_section = {}

for student in students:
    if student["group"] not in by_group:
        by_group[student["group"]] = []
    by_group[student["group"]].append(student)

    if student["section"] not in by_section:
        by_section[student["section"]] = []
    by_section[student["section"]].append(student)

# вывод результатов на экран
print("Учащиеся по группам:")
for group in by_group:
    print(f"Группа '{group}':")
    for student in by_group[group]:
        print(f"- {student['name']} ({student['section']})")

print()

print("Учащиеся по секциям:")
for section in by_section:
    print(f"Секция '{section}':")
    for student in by_section[section]:
        print(f"- {student['name']} ({student['group']})")
