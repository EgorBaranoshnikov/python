fin  = open("input.txt")
strings = fin.readlines()
a = strings[0].split()
b = int(a[0])
c = int(a[1])
ot = b ** c
print(ot)

