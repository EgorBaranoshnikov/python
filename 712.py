fin  = open("input.txt")
strings = fin.readlines()
stringsx = strings[0].split(' ')
n = int(stringsx[2])
w = int(stringsx[0])
h = int(stringsx[1])

min = 1

if w >= h:
    maxs = w
else:
    maxs = h
max = maxs * n




while(min < max):
    x = (max + min) // 2
    if ((x // w) * (x // h) >= n):
       max = x
    else:
       min = x + 1
print(max)