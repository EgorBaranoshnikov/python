fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
kol = int(mas[0])
st = int(mas[1])
fn = int(mas[2])
if st < fn:
    v1 = fn - st - 1
    v2 = kol - fn + st - 1
else:
    v1 = st - fn - 1
    v2 = kol - st + fn - 1

if v1 < v2:
    print(v1)
else:
    print(v2)