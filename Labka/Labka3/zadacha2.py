#используя функцию range() сделать список. в функцию range() введите данные
#с разными типами и выведите на экран в разных примерах.

"""ar = ("Hello world!")
for i in range(len(ar)):
    i+=1
print(";".join(list(ar)))"""
ar =[]
for i in (range(10,0,-1)):
    ar.append(i)
print(ar)

print("")
arr =["farhad",19,bool,4.55,[1,2,3,4]]
for i in range(len(arr)):
    i+=1
print(arr)
