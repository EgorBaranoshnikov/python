shislo = str(input("Введите четырёхзначное число"))

for i in range(1):
    if shislo[0] == shislo[1] == shislo[2] != shislo[3]:
        print("да")
        break
    if shislo[0] == shislo[1] == shislo[3] != shislo[2]:
        print("да")
        break
    if shislo[0] == shislo[3] == shislo[2] != shislo[1]:
        print("да")
        break
    if shislo[3] == shislo[1] == shislo[2] != shislo[0]:
        print("да")
        break
    else: 
        print("нет")
