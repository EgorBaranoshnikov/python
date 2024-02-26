fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
a = int(mas[0]) 
b = int(mas[1])


if a < b:
    min = a
    max = b
else:
    min = b
    max = a
if max % 2 == 0:
   otv1 = int((max // (max / 2)))
else:
    otv1 = int((max // (max / 2)) + 1)
otv2 = min
print(str(otv1)+ " " +str(otv2))