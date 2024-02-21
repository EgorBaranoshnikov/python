fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
max_min = int(mas[0])
tar1 = int(mas[1])
tar2 = int(mas[2])
kol_min = int(mas[3])
if kol_min <= max_min:
   otv = kol_min * tar1
if kol_min > max_min:
   max = max_min * tar1
   otv1 = (kol_min - max_min) * tar2
   otv = otv1 + max
print(otv)