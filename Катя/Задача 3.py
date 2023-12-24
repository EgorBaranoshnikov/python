shislo = str(input("Введите трёхзначное число"))

if shislo[1] < shislo[0] and shislo[2] < shislo[0]:
    print("1 цифра самое большая")
if shislo[0] < shislo[1] and shislo[2] < shislo[1]:
    print("2 цифра самое большая")
if shislo[0] < shislo[2] and shislo[1] < shislo[2]:
    print("3 цифра самое большая")