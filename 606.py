fin  = open("input.txt")
strings = fin.readlines()
shislo = strings[0].split(' ')
for i in range(1):
    if int(shislo[1]) <= int(shislo[0]) and int(shislo[2]) <= int(shislo[0]):
        if int(shislo[1]) + int(shislo[2]) > int(shislo[0]):
           print("YES")
           break
        else:
           print("NO")
           break
    if int(shislo[0]) <= int(shislo[1]) and int(shislo[2]) <= int(shislo[1]):
        if int(shislo[0]) + int(shislo[2]) > int(shislo[1]):
            print("YES")
            break
        else:
            print("NO")
            break
    if int(shislo[0]) <= int(shislo[2]) and int(shislo[1]) <= int(shislo[2]):
        if int(shislo[1]) + int(shislo[0]) > int(shislo[2]):
           print("YES")
           break
        else:
           print("NO")
           break