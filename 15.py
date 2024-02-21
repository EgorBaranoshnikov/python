fin  = open("input.txt")
strings = fin.readlines()
kol = int(strings[0])
mas1 = []
mas2 = []
otv = 0
for i in range(kol):
   w = strings[i + 1].split()
   for q in range(len(strings) - 1):
      m = int(w[q])
      if m == 1:
         otv += 1
otv = otv / 2
otv = int(otv)
print(otv)
