fin  = open("input.txt")
strings = fin.readlines()
mas = strings[1].split()
p1 = int(mas[0])
kol = int(strings[0])
ind = 1
otv = 0
for i in range(kol - 1):
   otv += int(mas[ind]) - 1
   ind += 1
otv = otv + p1
print(otv)