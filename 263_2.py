fin = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
kol = int(mas[0])
st = int(mas[1])
fn = int(mas[2])
stp = st
stm = st
if st == kol:
    stp = 0
for i in range(kol):
    stp += 1
    stm -= 1
    if stm == 0:
        stm = kol
    if stp == kol:
        stp = 0
    if stm == fn:
        print(i)
        break
    if stp == fn:
        print(i)
        break
