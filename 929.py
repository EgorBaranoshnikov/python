fin  = open("input.txt")
strings = fin.readlines()
a = int(strings[0]) 
otv_2 = a * 6
q = int(a / 6)
w = a - q * 6
if w == 1:
    otv_1 = q + 6
if w == 2:
    otv_1 = q + 5
if w == 3:
    otv_1 = q + 4
if w == 4:
    otv_1 = q + 3
if w == 5:
    otv_1 = q + 2
if w == 6:
    otv_1 = q + 1
if w == 0:
    otv_1 = q + 0
print(otv_1, otv_2)