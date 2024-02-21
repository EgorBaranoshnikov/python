fin  = open("input.txt")
strings = fin.readlines()
a = int(strings[0])

if a < 10:
    b = "000"+str(a)
elif a < 100:
    b = "00"+str(a)
elif a < 1000:
    b = "0"+str(a)
else:
    b = a
       


if a % 400 == 0:
    print("12/09/"+str(b))
else:    
    if a % 4 == 0:
        if a % 100 != 0:
            print("12/09/"+str(b))
        
        else:
            print("13/09/"+str(b))
        
    else:
        print("13/09/"+str(b))