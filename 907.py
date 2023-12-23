fin  = open("input.txt")
strings = fin.readlines()
stringsx = strings[0].split(' ')
w = int(stringsx[0])
h = int(stringsx[1])
r = int(stringsx[2])
d = r * 2
if d <= w and d <= h:
    print("YES")
else:
    print('NO')