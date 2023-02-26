while True:
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        break
    else:
        print("Both inputs must be valid numbers.")

print(f"The sum of {a} and {b} is: {a + b}")

