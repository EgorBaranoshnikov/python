fin  = open("input.txt")
strings = fin.readlines()
a = int(strings[0])
c = 0
d = 0
q = 0
if a > 0:
   q = a * 1
if a < 0:
   q = a * -1
if a == 0:
   print("1")
else:   
    for i in range(0, q):
        if a > 0:
            c += 1
            d += c
            e = d
        if a < 0:
            c += 1
            d += c
            w = d - 1
            e = w * -1
    print(e)