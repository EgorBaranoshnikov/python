fin  = open("input.txt")
strings = fin.readlines()
mas1 = strings[0].split()
x1 = int(mas1[0]) 
y1 = int(mas1[1])
r1 = int(mas1[2])
mas2 = strings[1].split()
x2 = int(mas2[0]) 
y2 = int(mas2[1])
r2 = int(mas2[2])

if x1 > x2:
    kat1 = x1 - x2
else:
    kat1 = x2 - x1
if y1 > y2:
    kat2 = y1 - y2
else:
    kat2 = y2 - y1
gip = (kat1 ** 2 + kat2 ** 2) ** 0.5



if r1 > r2:
    a = r2
    b = r1
else:
    a = r1
    b = r2
if gip + a < b:
    print("NO")
else:


    if gip <= r1 + r2:
        print("YES")
    else:
        print("NO")