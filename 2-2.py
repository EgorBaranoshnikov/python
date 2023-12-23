fin  = open("input.txt")
strings = fin.readlines()
stringsx = strings[0].split(' ')
if (len(stringsx)) == 1:
   ot = 1
   do = int(stringsx[0])
if (len(stringsx)) > 1:
   ot = int(stringsx[0])
   do = int(stringsx[1])
po = 1
d = 0
sum = 0
if do > 0:
   do += 1
if do < 0:
   po = -1
   do -= 1
if do == 0:
   po = -1
for i in range(ot, do, po):
   sum += i
print(sum)