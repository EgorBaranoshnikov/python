fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
ind_ch = int(mas[0]) 
ch1 = int(mas[1])
ch2 = int(mas[2])

for i in range(1):
    if ind_ch == 1:
        print(ch1, ch2)
        break
    if ind_ch == 2:
        print(ch2 - ch1, ch1)
        break
    bol = ch2
    men = ch1
    for i in range(ind_ch - 2):
        a = bol - men
        bol = men
        men = a
    d = a
    a = bol - men
    print(a, d)             