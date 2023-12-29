fin  = open("input.txt")
strings = fin.readlines()
vse_byk = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "q" ]
ind = 0
estOtvet = False

for i in range(26):
    ceshac = vse_byk[ind]
    if ceshac == strings[0].replace("\n", ""):
        if  ind == 25:
           print("q")
           estOtvet = True
           break
        else:
           print(vse_byk[ind + 1])
           estOtvet = True
           break
    ind += 1

if estOtvet is False:
    print("")