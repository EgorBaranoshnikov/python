fin  = open("input.txt")
strings = fin.readlines()

ras = 0
otv = 0

nach = int(strings[0])
ind = 2
x1 = 0
y1 = 0
f = strings[1].split()
x2 = int(f[0])
y2 = int(f[1])
for i in range(nach + 1):

    if x1 >= x2:
        x = x1 - x2
    else:
        x = x2 - x1
    if x1 >= x2:
        y = y1 - y2
    else:
        y = y2 - y1

    ras1 = x ** 2 + y ** 2
    ras = ras1 ** 0.5
    otv += ras



    x1 = x2
    y1 = y2

    if ind == nach + 1:
        x2 = 0
        y2 = 0
    else:
        stra = strings[ind].split()
        x2 = int(stra[0])
        y2 = int(stra[1])
        ind += 1

kol1 = str(otv)
kol = len(kol1)
if kol == 3:
    kol1 = kol1 + "00"
if kol == 2:
    kol1 = kol1 +"0"
if kol >= 5:
    kol1 = round(otv, 3)
print(kol1)             