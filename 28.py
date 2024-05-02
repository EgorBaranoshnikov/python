fin  = open("input.txt")
strings = fin.readlines()
f = strings[0].split()
x1 = int(f[0])
y1 = int(f[1])
x2 = int(f[2])
y2 = int(f[3])

k = strings[1].split()
x = int(k[0])
y = int(k[1])

if x1 == x2:
    if x1 < x:
        q = x - x1
        x_otv = x1 - q
    else:
        q = x1 - x
        x_otv = x1 + q
    y_otv = y

if y1 == y2:
    if y1 < y:
        q = y - y1
        y_otv = y1 - q
    else:
        q = y1 - y
        y_otv = y1 + q
    x_otv = x

print(x_otv, y_otv) 