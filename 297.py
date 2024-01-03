fin  = open("input.txt")
chislo = fin.readlines()


ind = 0
kol = 0
for i in range(len(chislo[0])):
    cech = chislo[0][ind]
    if cech == "0" or cech == "6" or cech == "9":
       kol += 1
    if cech == "8":
        kol += 2
    ind += 1
print(kol)
        