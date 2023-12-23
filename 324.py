fin  = open("input.txt")
strings = fin.readlines()
str = strings[0]
q = 0

if str[0] == str[3]:
    q += 1
if str[1] == str[2]:
    q += 1
if q == 2:
    print("YES")
else:
    print("NO")