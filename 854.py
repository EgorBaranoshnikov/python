fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
room = int(mas[0])
cond = int(mas[1])
rech = strings[1].rstrip()
if rech == "freeze":
    if cond < room:
        print(cond)
    else:
        print(room)
if rech == "heat":
    if cond > room:
        print(cond)
    else:
        print(room)
if rech == "auto":
    print(cond)
if rech == "fan":
    print(room)

