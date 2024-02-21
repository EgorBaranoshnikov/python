fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
a = int(mas[0]) # кол строк
b = int(mas[1]) # кол столбцов
c = int(mas[2]) # искомая строка
d = int(mas[3]) # искомый столбик
if c % 2 == 0:
   k = (c - 1) * b # числа до искомой строчки
   f = b - d # 
   otv = k + f
   
else:
   k = (c - 1) * b
   otv = k + d
   otv = otv - 1
print(otv)