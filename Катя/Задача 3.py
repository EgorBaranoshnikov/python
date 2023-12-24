shislo = str(input("Введите трёхзначное число: "))

if int(shislo[0]) > int(shislo[2]):
    print("a) первая цифра больше последней")
if int(shislo[2]) > int(shislo[0]):
    print("a) последняя цифра больше первой")

if int(shislo[0]) > int(shislo[1]):
    print("b) первая цифра больше второй")
if int(shislo[1]) > int(shislo[0]):
    print("b) вторая цифра больше первой")

if int(shislo[1]) > int(shislo[2]):
    print("c) вторая цифра больше последней")
if int(shislo[2]) > int(shislo[1]):
    print("c) последняя цифра больше второй")
