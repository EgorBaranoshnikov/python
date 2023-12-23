fin  = open("input.txt")
strings = fin.readlines()
pr1 = 0
ind = 1
ind1 = 0
ot = 0
do = 0
a = 0
otv = []
ind = 1
indi = 0
p = 0
c = 0
pred = []
v = 0
for i in range(len(strings) - 1):
    strings1 = strings[ind].split()
    ind += 1
    for i in range(len(strings1)):
        str1 = int(strings1[ind1])
        pr1 += 1
        if pr1 == 1:
            ot = str1
        if pr1 == 2:
            do = str1
        ind1 += 1
    pr1 = pr1 -pr1
    ind1 = ind1 - ind1
    ot1 = ot
    do1 = do
    for q in range(ot, do + 1):
       otv.insert(ot1, q) 
       ot1 += 1
    pred.append(otv)
    otv = []
    p += 1

for e in range():
    for w in pred:
        if e in w:
           a += 1
    if a == len(strings) - 1:
        v +=1
    a = 0
if v > 0:
    print("YES")
else:
    print("NO")