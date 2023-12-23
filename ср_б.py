fin  = open("input.txt")
strings = fin.readlines()

q = 0
b = 0
e = 0
w2 = 0
w3 = 0
w4 = 0
w5 = 0

for i in range(len(strings)):
    a = strings[q]
    q += 1
    if  a != 'вЂў\n' or a != '!\n' or a != 'вЂў' or a != '!' or a != 'Рќ\n' or a != 'Рќ':
        c = int(a)
        b += c
        if c == 2:
           w2 += 1
        if c == 3:
           w3 += 1
        if c == 4:
           w4 += 1
        if c == 5:
           w5 += 1
        e += 1


if e == 0:
    print("у тебя нет оценок")
else:
    t = b / e
    print("СРЕДНИЙ БАЛ")
    print(t)


z2 = w2 * 5
z3 = w3 * 3
z4 = w4 * 1
vse1 = z2 + z3 + z4 - w5
if vse1 < 0:
    vse1 = 0
print("====================================")
print("кол. 5 до 5")
print(vse1)
print("====================================")


vse2 = w2 + w3 - w5
if w3 <= w4:
    vse2 -= w4
if vse2 < 0:
    vse2 = 0

x2 = w2 * 3
vse3 = x2 + w3 - w4
if w5 >= w2:
   vse3 -= 3
if vse3 < 0:
    vse3 = 0
print("====================================")
print("кол. 5 до 4")
print(vse2)
print("кол. 4 до 4")
print(vse3)
print("====================================")