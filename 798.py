fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
rid = int(mas[0])
stol = int(mas[1])
kl_rid = int(mas[2])
kl_stol = int(mas[3])
c = int(mas[4])

#if kl_rid != 1:
#    if kl_rid % 2 == 0:
#        if c == 1:
#            c = 0
#        if c == 0:
#            c = 1
#    kl_rid = 1
#if kl_stol != 1:
#    if kl_stol % 2 == 0:
#        if c == 1:
#            c = 0
#        if c == 0:
#            c = 1
#    kl_stol = 1



if (rid * stol) % 2 == 0:
   print("equal")
else:
    if (kl_rid + kl_stol) % 2 == 0:
        if c == 1:
            c = "white"
        if c == 0:
            c = "black"
        print(c)
    else:
        if c == 0:
            c = "white"
        if c == 1:
            c = "black"
        print(c)