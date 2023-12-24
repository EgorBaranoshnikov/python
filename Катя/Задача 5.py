shislo = str(input("Введите трёхзначное число"))

if int(shislo[1]) <= int(shislo[0]) and int(shislo[2]) <= int(shislo[0]):
    #1 цифра самое большая
    if int(shislo[1]) > int(shislo[2]):
        #2 цифра поменьше
        otv = int(shislo[0]) + int(shislo[1])
    else:
        #3 цифра поменьше
        otv = int(shislo[0]) + int(shislo[2])
                                  

if int(shislo[0]) <= int(shislo[1]) and int(shislo[2]) <= int(shislo[1]):
    #2 цифра самое большая
    if int(shislo[0]) > int(shislo[2]):
        #1 цифра поменьше
        otv = int(shislo[1]) + int(shislo[0])
    else:
        #3 цифра поменьше
        otv = int(shislo[1]) + int(shislo[2])
                                  

if int(shislo[0]) <= int(shislo[2]) and int(shislo[1]) <= int(shislo[2]):
    #3 цифра самое большая
    if int(shislo[0]) > int(shislo[1]):
        #1 цифра поменьше
        otv = int(shislo[2]) + int(shislo[0])
    else:
        #2 цифра поменьше
        otv = int(shislo[2]) + int(shislo[1])
print(otv)