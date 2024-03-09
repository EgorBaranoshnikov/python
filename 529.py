fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
x1 = int(mas[0]) 
y1 = int(mas[1])
x2 = int(mas[2])
y2 = int(mas[3])


if x1 >= x2:
   ka1 = x1 - x2
else:
   ka1 = x2 - x1
if y1 > y2:
   ka2 = y1 - y2
else:
   ka2 = y2 - y1
    

a = ka1 ** 2
b = ka2 ** 2
otv = (a + b) ** 0.5


a = int(otv) 
if a - otv == 0:
   otv = int(otv)
else:
   otv = round(otv, 5)


print(otv)