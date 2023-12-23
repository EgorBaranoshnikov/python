fin  = open("input.txt")
strings = fin.readlines()
kol = int(strings[0])
ind = 1




for i in range(kol):
    stringsx = strings[ind].split(' ')
    n = int(stringsx[0])
    m = int(stringsx[1])
    otv = 19 * m + (n + 239)*(n + 366) / 2 
    otv = int(otv)
    print(otv)
    ind += 1