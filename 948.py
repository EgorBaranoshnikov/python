fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
kol_ctrok = int(mas[0]) 
nom_ctrok = int(mas[1])
ch1 = nom_ctrok // kol_ctrok + 1
ch2_1 = kol_ctrok * (ch1 - 1)
ch2 = nom_ctrok - ch2_1
if nom_ctrok % kol_ctrok == 0:
    ch1 = ch1 - 1
    ch2 = kol_ctrok
print(ch1, ch2)