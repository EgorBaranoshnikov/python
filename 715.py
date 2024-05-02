fin  = open("input.txt")
strings = fin.readlines()
f = strings[0].split()
x = int(f[0])
y = int(f[1])
otv = 0
for i in range(x):
    k = strings[1 + i].split()
    l = strings[2 + x + i].split()
    for o in range(y):
        n = k[0][o]
        m = l[0][o]
        if n == m:
            otv += 1
print(otv)