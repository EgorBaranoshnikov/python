fin  = open("input.txt")
strings = fin.readlines()
rp = int(strings[0])
for i in range(1):
    if rp == 1:
        print("VGC")
        break
    if rp == 2:
        print("CVG")
        break




    if rp % 3 == 0:
        print("GCV")
    if rp % 3 == 2:
        print("CVG")
    if rp % 3 == 1:
        print("VGC")

