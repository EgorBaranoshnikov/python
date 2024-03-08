fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
ind_ch = int(mas[0]) 
ch1 = int(mas[1])
ch2 = int(mas[2])


bol = ch2
men = ch1
for i in range(ind_ch - 2):
    a = bol - men
    bol = men
    men = a
d = a
a = bol - men
print(d, a)             