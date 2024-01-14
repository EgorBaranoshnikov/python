
fin  = open("input.txt")
strings = fin.readlines()
mas = strings[1].split()

max = 0
tek = 0
ind = 0

for i in range(int(strings[0])):
    if int(mas[ind]) > 0:
       tek += 1
       if tek > max:
           max = tek
    else:
        tek = 0
    ind += 1
print(max)