grades = {
    'farhad': {'математика': 5, 'физика': 4, 'география': 3},
    'murod': {'математика': 3, 'физика': 5, 'география': 4},
    'baha': {'математика': 4, 'физика': 5, 'география': 4},
}

name = input('Введите имя учащегося: ')

if name in grades:
    print(f"Оценки учащегося {name}:")
    for subject, grade in grades[name].items():
        print(f"{subject}: {grade}")
else:
    print(f"Учащийся {name} не найден.")
