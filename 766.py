fin  = open("input.txt")
strings = fin.readlines()
a = strings[0].split()
b = int(a[0])
c = int(a[1])
d = int(a[2])

q = b * c
if q == d:
    print("YES")
if q > d:
    print("YES")
if q < d:
    print("NO")