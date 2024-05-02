fin  = open("input.txt")
strings = fin.readlines()
ind = 1
otv = 0

if len(strings[0]) < 5:
    print(0)
else:
    if strings[0][ind] == "-" and strings[0][ind + 1] == "-":
        if strings[0][ind + 2] == "<" and strings[0][ind + 3] == "<" and strings[0][ind - 1] == "<":
                otv += 1
    ind += 1
    for i in range(len(strings[0]) - 4):
        if strings[0][ind] == "-" and strings[0][ind + 1] == "-":
            if strings[0][ind - 1] == ">" and strings[0][ind - 2] == ">" and strings[0][ind + 2] == ">":
                otv += 1
            if strings[0][ind + 2] == "<" and strings[0][ind + 3] == "<" and strings[0][ind - 1] == "<":
                otv += 1
        ind += 1

    print(otv)