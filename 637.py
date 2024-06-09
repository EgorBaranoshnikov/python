fin  = open("input.txt")
strings = fin.readlines()
mas = strings[1].split()
kol = int(strings[0])
chal = int(strings[2])
ind = 0
indm = 0
otv = 0

for i in range(kol):
   tek = int(mas[ind])
   if tek <= chal:
      otv += tek
   if tek > chal:
      otv += chal
   ind += 1
print(otv)