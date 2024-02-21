fin  = open("input.txt")
strings = fin.readlines()
shuc = strings[0][0]
shuf = int(strings[0][1])
if shuf % 2 == 0:
    if shuc == "A" or shuc == "C" or shuc == "E" or shuc == "G":
        print("WHITE")
    else:
        print("BLACK")
else:
    if shuc == "A" or shuc == "C" or shuc == "E" or shuc == "G":
        print("BLACK")
    else:
        print("WHITE")