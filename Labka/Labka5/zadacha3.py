numbers = []
while True:
    num = int(input("Введите число (0 для выхода): "))
    if num == 0:
        break
    numbers.append(num)

numbers.sort(reverse = True)
print(f"Введенные числа (в порядке возрастания): {numbers}")
