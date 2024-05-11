fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
str = int(mas[0])
sto = int(mas[1])
ind1 = 0
ind2 = 0
a = 0
for i in range(str):
    sp1 = strings[ind1 + 1].split()
    sp2 = strings[ind1 + str + 1].split()
    for i in range(sto):
        if int(sp2[ind2]) == 0:
            if sp1[0][ind2] != ".":
                a += 1               
        if int(sp2[ind2]) == 1:
            if sp1[0][ind2] != "." and sp1[0][ind2] != "B":
                a += 1
        if int(sp2[ind2]) == 2:
            if sp1[0][ind2] != "." and sp1[0][ind2] != "G":               
                a += 1                
        if int(sp2[ind2]) == 3:
            if sp1[0][ind2] != "." and sp1[0][ind2] != "G" and sp1[0][ind2] != "B":                
                a += 1                
        if int(sp2[ind2]) == 4:
            if sp1[0][ind2] != "." and sp1[0][ind2] != "R":                
                a += 1                
        if int(sp2[ind2]) == 5:
            if sp1[0][ind2] != "." and sp1[0][ind2] != "R" and sp1[0][ind2] != "B":                
                a += 1                
        if int(sp2[ind2]) == 6:
            if sp1[0][ind2] != "." and sp1[0][ind2] != "R" and sp1[0][ind2] != "G":                
                a += 1                
        if int(sp2[ind2]) == 7:
            if sp1[0][ind2] != "." and sp1[0][ind2] != "R" and sp1[0][ind2] != "G" and sp1[0][ind2] != "B":                
                a += 1               
        ind2 += 1
    ind1 += 1
    ind2 = 0
if a > 0:
    print("NO")
else:  
    print("YES")