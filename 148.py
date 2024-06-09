fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
a = int(mas[0])
b = int(mas[1])
if a >= b:
    min = b
else:
    min = a
tek = min
for i in range(1):
    if a % tek == 0 and b % tek == 0:
        print(tek)
        break
    min = round(min / 2 + 1)
    tek = min
    for i in range(min):
        if a % tek == 0 and b % tek == 0:
            print(tek)
            break
        tek -= 1
