fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
p1 = int(mas[0])
p2 = int(mas[1])
p3 = int(mas[2])
prov = 0
for i in range(1):
    if p1 + p2 == p3 or p2 + p1 == p3:
        print("YES")
        prov += 1
        break
    if p1 + p3 == p2 or p3 + p1 == p2:
        print("YES")
        prov += 1
        break
    if p2 + p3 == p1 or p3 + p2 == p1:
        print("YES")
        prov += 1
        break
if prov == 0:
    print("NO")