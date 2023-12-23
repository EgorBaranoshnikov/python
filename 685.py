fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
w1 = 0
w2 = 0
w3 = 0

k1 = 0
k2 = 0
k3 = 0

ind = 0
ind1 = 0
ind2 = 0

in0 = 3
in1 = 3
in2 = 3

a = -1
b = -1

c = 2
d = 2
for i in range(len(mas) - 3):
    if w3 < int(mas[ind]):
       w3 = int(mas[ind])
       a += 1
    ind += 1
for i in range(len(mas) - 4):
    if ind1 == a:
       ind1 += 1 
    if w2 < int(mas[ind1]):
        w2 = int(mas[ind1])
        b += 1
    ind1 += 1
for i in range(len(mas) - 5):
    if ind2 == b:
       ind2 += 1 
    if ind2 == a:
       ind2 += 1 
    if w1 < int(mas[ind2]):
        w1 = int(mas[ind2])


for i in range(len(mas) - 3):
    if k3 < int(mas[in0]):
       k3 = int(mas[in0])
       c += 1
    in0 += 1
for i in range(len(mas) - 4):
    if in1 == c:
       in1 += 1 
    if k2 < int(mas[in1]):
        k2 = int(mas[in1])
        d += 1
    in1 += 1
for i in range(len(mas) - 5):
    if in2 == d:
       in2 += 1 
    if in2 == c:
       in2 += 1 
    if k1 < int(mas[in2]):
        k1 = int(mas[in2])
otv1 = w3 * k3
otv2 = w2 * k2
otv3 = w1 * k1
otv = otv1 + otv2 + otv3
print(otv)