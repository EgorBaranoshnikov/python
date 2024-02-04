fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
sh = int(mas[0])
dl = int(mas[1])
v = int(mas[2])

m2 = sh * v
m3 = dl * v

met = 2 * (m2 + m3)

otv = met / 16
if met % 16 == 0:
   otv = int(otv)
   print(otv)
else:
   otv = int(otv)
   print(otv + 1)