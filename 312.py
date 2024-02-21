fin  = open("input.txt")
strings = fin.readlines()
mas1 = strings[0].split()
p1 = int(mas1[0])
p2 = int(mas1[1])
p3 = int(mas1[2])
d = p2 - p1
for i in range(p3 - 1):
    p1 += d
print(p1)