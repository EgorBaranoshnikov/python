fin  = open("input.txt")
strings = fin.readlines()
pr = 0
ind = 1
ind1 = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0
pr1 = 0
pr2 = 0
x = 0
y = 0
prv = 0
otv = 0
x11 = 0
x22 = 0
y11 = 0
y22 = 0
a = 0
b = 0
c = 0
d = 0
inde1 = 0
xbc1 = 0

for i in range(len(strings) - 1):
    strings1 = strings[ind].split()
    for i in range(len(strings1)):
        str1 = int(strings1[ind1])
        ind1 += 1
        pr += 1
        if pr == 1:
           x = str1 
        if pr == 2:
           y = str1
        
        if pr > 2:
            if pr == 3 or pr == 5 or pr == 7 or pr == 9:
                pr1 += 1
                if str1 > x1:
                   x1 = str1
                   inde1 = ind1
                if pr1 == 1:
                   x2 = str1
                   inde2 = ind1
                if str1 < x2:
                   x2 = str1
                   inde2 = ind1
            if pr == 4 or pr == 6 or pr == 8 or pr == 10:
                pr2 += 1
                if str1 > y1:
                   y1 = str1
                   inde3 = ind1
                if pr2 == 1:
                    y2 = str1
                    inde4 = ind1
                if str1 < y2:
                   y2 = str1
                   inde4 = ind1
            if x1 > strings1[0]:
                xbc1 = strings1[0] - xbc1
            if x1 < strings1[0]:
                xbc1 = xbc1 - strings1[0]
    ind1 = 0
    ind += 1
    if x1 >= x:
        prv += 1
    if x2 <= x:
        prv += 1
    if y1 >= y:
        prv += 1
    if y2 <= y:
        prv += 1
    if prv == 4:
        otv += 1
    pr = pr - pr
    pr1 = pr1 - pr1
    pr2 = pr2 - pr2
    prv = prv - pr
    a = inde1
    b = inde2 -2
    c = inde3
    d = inde4 -2
    print(x1, x2, y1, y2)
    print(strings1[a], strings1[b], strings1[c], strings1[d])
    print(xbc1)
print(otv)