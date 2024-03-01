fin  = open("input.txt")
strings = fin.readlines()
a = int(strings[0])
ind = 3
b = 1
while True:
    while ind != a // 2:
        if a % ind == 0:
           a += 2
           b = ""
           break
        else:
            ind += 1
    ind = 2
    if b != "":
        print(a)
        a += 2
    b = 1
        