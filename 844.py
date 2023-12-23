fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
c1 = int(mas[0])
c2 = int(mas[1])
p = c1 * c2
otv = p ** 0.5
o = round(otv)
if otv == o:
    print(int(otv))
else:
    print(0)