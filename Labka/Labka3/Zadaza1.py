# Написать программу используя цикл for и while.
a = int(input('№ '))
list = []
i=0
while i< a:
    string = "Enter element №" + str(i+1) +": "
    list.append((input(string)))
    i+=1
print(list)
