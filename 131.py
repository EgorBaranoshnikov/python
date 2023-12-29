fin  = open("input.txt")
strings = fin.readlines()
stringsx = int(strings[0])

max = 0
maxi = 0
ind = 1

for i in range(stringsx):
    a = strings[ind].split()
    if int(a[1]) == 1:
        if int(a[0]) > max:
            max = int(a[0])
            maxi = i + 1
    ind += 1
if max == 0:
   print("-1")
else:
   print(maxi)

