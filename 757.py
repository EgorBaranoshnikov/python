fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
C = int(mas[0]) 
H = int(mas[1]) 
O = int(mas[2])
kol_C = C // 2
kol_H = H // 6
kol_O = O

if kol_C <= kol_H and kol_C <= kol_O:
    print(kol_C)
elif kol_H <= kol_C and kol_H <= kol_O:
    print(kol_H)
elif kol_O <= kol_C and kol_O <= kol_H:
    print(kol_O)