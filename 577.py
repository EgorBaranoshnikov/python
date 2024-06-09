fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
a = int(mas[0])
b = int(mas[1])

q_0 = 0
q_1 = 0
q_2 = 0
q_3 = 0
q_4 = 0
q_5 = 0
q_6 = 0
q_7 = 0
q_8 = 0
q_9 = 0

for i in range(a):
    for w in range(b):
       for e in range(len(str(((i + 1) * (w + 1))))):
            s = (i + 1) * (w + 1)
            f = str(len(s))
            if str(len(s)) == 0:
                q_0 += 1
            if str(len(s)) == 1:
                q_1 += 1
            if str(len(s)) == 2:
                q_2 += 1
            if str(len(s)) == 3:
                q_3 += 1
            if str(len(s)) == 4:
                q_4 += 1
            if str(len(s)) == 5:
                q_5 += 1
            if str(len(s)) == 6:
               q_6 += 1
            if str(len(s)) == 7:
               q_7 += 1
            if str(len(s)) == 8:
               q_8 += 1
            if str(len(s)) == 9:
               q_9 += 1