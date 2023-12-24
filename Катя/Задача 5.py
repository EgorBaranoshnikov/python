shislo = str(input("Введите трёхзначное число"))

if shislo[1] <= shislo[0] and shislo[2] <= shislo[0]:
    #1 цифра самое большая
    if shislo[1] > shislo[2]:
        #2 цифра поменьше
        otv = int(shislo[0]) + int(shislo[1])
    else:
        #3 цифра поменьше
        otv = int(shislo[0]) + int(shislo[2])
                                  



if shislo[0] <= shislo[1] and shislo[2] <= shislo[1]:
    #2 цифра самое большая
    if shislo[0] > shislo[2]:
        #1 цифра поменьше
        otv = int(shislo[1]) + int(shislo[0])
    else:
        #3 цифра поменьше
        otv = int(shislo[1]) + int(shislo[2])
                                  



if shislo[0] <= shislo[2] and shislo[1] <= shislo[2]:
    #3 цифра самое большая
    if shislo[0] > shislo[1]:
        #1 цифра поменьше
        otv = int(shislo[2]) + int(shislo[0])
    else:
        #2 цифра поменьше
        otv = int(shislo[2]) + int(shislo[1])
print(otv)