fin  = open("input.txt")
strings = fin.readlines()
kol = int(strings[0])
if kol == 1:
   print(1)
if kol == 0:
   print(0)
if kol > 1:
    a = 1
    f = 1
    for i in range(kol):
        if f <= kol:
            a += 1
            f += a
        else:
            print(a - 1)
            break