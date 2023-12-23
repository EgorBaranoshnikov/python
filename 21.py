fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
pr = 0
ind = 0
min = 0
max = 0
for i in range(len(mas)):
   x = int(mas[ind])
   if pr == 0:
      min = x
   if min > x:
      min = x
   if max < x:
      max = x
   ind += 1
   pr += 1
otv = max - min
print(otv)