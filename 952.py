fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
vsr = int(mas[0])
det = int(mas[1])
if vsr == 0 and det > 0:
    print("Impossible")
else:
    if det >= vsr:
        min = vsr + (det - vsr) 
    if det < vsr:
        min = vsr
    if det > 0:
        max = vsr + (det - 1)
    if det == 0:
        max = vsr
    print(min, max)