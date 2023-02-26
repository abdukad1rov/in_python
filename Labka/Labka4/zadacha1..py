# 1. len() - для получения длины строки
string = "Hello World!"
print("Длина строки:", len(string),'\n')

# 2. strip() - для удаления пробелов с обоих концов строки
string = "   Hello World!   "
print("Конечный результат:", string.strip(),'\n')

# 3. split() - для разделения строки на список на основе указанного разделителя
string = "Hello"
print("Разделённый строка:", string.split(","),'\n')

# 4. replace() - для замены указанной подстроки другой строкой
string = "Hello World!"
print("Замененная строка:", string.replace("World", "Universe"),'\n')

# 5. upper() - для преобразования всех символов строки в верхний регистр
string = "Hello World!"
print("Строка в верхнем регистре:", string.upper(),'\n')

# 6. lower() - для преобразования всех символов строки в нижний регистр
string = "Hello World!"
print("Строка в нижнем регистре:", string.lower(),'\n')

# 7. count() - для подсчета количества вхождений подстроки в строку
string = "Hello World, welcome to the World!"
print("Количество 'o':", string.count("o"),'\n')

# 8. startswith() - для проверки, начинается ли строка с указанного префикса
string = "Hello World!"
print("Начинается с 'Hello':", string.startswith("Hello"),'\n')

# 9. endswith() - для проверки, заканчивается ли строка указанным суффиксом
string = "Hello World!"
print("Заканчивается на !:", string.endswith("!"),'\n')

# 10. join() - для объединения элементов списка с указанным разделителем
list = ["Hello", "World", "!"]
separator = ","
print("Присоединиться к списку:", separator.join(list),'\n')
