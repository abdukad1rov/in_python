def is_sorted_asc(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
def is_sorted_desc(lst):
    return all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
my_list = []
while True:
    num = int(input("Введите число (0 для выхода): "))
    if num == 0:
        break
    my_list.append(num)

if is_sorted_asc(my_list):
    print(True)
else:
    print(False)
