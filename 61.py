fin  = open("input.txt")

 
strings = fin.readlines()



q = strings[0].split()
p = strings[1].split()
o = strings[2].split()
v = strings[3].split()
e = int(q[0])
f = int(q[1])
g = int(p[0])
h = int(p[1])
i = int(o[0])
k = int(o[1])
l = int(v[0])
m = int(v[1])


k1 = 0
k2 = 0

oo = e + g + i + l
k1 += oo

ss = f + h + k + m
k2 += ss

if k1 < k2:
   print("2")
if k1 > k2:
    print("1")
if k1 == k2:
   print("DRAW")