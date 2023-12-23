fin  = open("input.txt")
strings = fin.readlines()
strings1 = strings[0].split()
str1 = int(strings1[0])
if str1 % 2 == 0:
    otv = str1 / 2
    print(int(otv))
if str1 % 2 > 0 and str1 > 1:
    print(str1)
if str1 == 1:
    print(0)