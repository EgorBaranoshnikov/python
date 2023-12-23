fin  = open("input.txt")
strings = fin.readlines()
stringsx = strings[0].split(' ')
rp = int(stringsx[0]) * 2
pk1 = int(stringsx[1]) * 2
pk2 = int(stringsx[2]) * 2
if pk1 + pk2 <= rp:
    print("YES")
else:
    print("NO")