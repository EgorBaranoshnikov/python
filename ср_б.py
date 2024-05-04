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