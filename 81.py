fin  = open("input.txt")
strings = fin.readlines()
mas = strings[1].split()
ind = -1
min = 0
max = 0
pr = 0
for i in range(len(mas)):
   pr += 1
   ind += 1
   mas1 = mas[ind]
   mas2 = int(mas1)
   if pr == 1:
      min = mas2
   if mas2 < min:
      min = mas2
   if mas2 > max:
      max = mas2
print(min, max)