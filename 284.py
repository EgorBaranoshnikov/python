fin  = open("input.txt")
strings = fin.readlines()
mas1 = strings[1].split()
p1 = int(strings[0])
p2 = int(strings[2])
ind = 3
otv = []
for i in range(p2):
   # print(otv)
   # otv = []
    f = strings[ind].split()
    ind1 = f[0]
    ind2 = f[1]
    ind += 1
    for i in range(int(ind2) - int(ind1) + 1):
        otv.append(mas1[int(ind1) - 1])
        ind1 = int(ind1) + 1
    otv = " ".join(otv)
    print(otv)
    otv = []