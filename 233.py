fin  = open("input.txt")
strings = fin.readlines()
mas = strings[1].split()
kol = int(strings[0])
ind = -1
pro = 0
prov = 0
for i in range(kol):
    ind += 1
    if int(mas[ind]) <= 437:
      print("Crash", i + 1)
      prov += 1
      break
if prov == 0: 
   print("No crash")