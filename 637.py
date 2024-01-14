fin  = open("input.txt")
strings = fin.readlines()
mas = strings[1].split()
kol = int(strings[0])
chal = int(strings[2])
ind = 0
indm = 0
otv = 0

for i in range(kol * chal):
   tek = int(mas[ind])
   if tek == 0:
      indm += 1
   else:
      mas[ind] = tek - 1
      otv += 1
   ind += 1 
   if ind == kol:
      ind = indm
      chal -= 1
      if chal == 0:
        break
print(otv)
