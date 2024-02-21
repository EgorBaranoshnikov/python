fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
kol = 0
ind = 0
for i in range(len(mas)):
   kol += int(mas[ind])
   ind += 1
otv = kol / 27
otv = int(otv)
print(otv)