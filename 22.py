fin  = open("input.txt")
strings = fin.readlines()
x = int(strings[0])

a = 1
kol_ch = 0
while a <= x:
    a = a * 2
    kol_ch += 1


otv = 0
a = a / 2
tek_v = x
for i in range(kol_ch):
   tek_v = tek_v - a
   if tek_v >= 0:
       otv += 1
   else:
       tek_v = tek_v + a
   a = a / 2
print(otv)