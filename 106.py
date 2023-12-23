fin  = open("input.txt")
strings = fin.readlines()
kol = int(strings[0])
ore = 0
reh = 0
ind = 1
for i in range(kol):
    if int(strings[ind]) == 1:
       ore += 1
    else:
       reh += 1
    ind += 1
if ore < reh:
   print(ore)
else:
   print(reh)