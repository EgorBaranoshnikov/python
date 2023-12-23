fin  = open("input.txt")
strings = fin.readlines()
mas = strings[1].split()
ind = 0
pr = 0
o = 0
for i in range(len(mas)):
        str1 = int(mas[ind])
        if pr == 0:
            otv = str1 + int(mas[ind + 1]) + int(mas[len(mas) - 1])
        if pr == len(mas) - 1:
            otv = str1 + int(mas[0]) + int(mas[ind - 1])
        if pr > 0 and pr < len(mas) - 1:
            otv = str1 + int(mas[ind + 1]) + int(mas[ind - 1])
        ind += 1
        pr += 1
        if otv > o:
           o = otv
print(o)