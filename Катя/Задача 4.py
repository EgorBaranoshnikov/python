shislo = str(input("Введите четырёхзначное число: "))

if shislo[0] == shislo[1] == shislo[2] != shislo[3]:
    print("да")    
elif shislo[0] == shislo[1] == shislo[3] != shislo[2]:
    print("да")    
elif shislo[0] == shislo[3] == shislo[2] != shislo[1]:
    print("да")    
elif shislo[3] == shislo[1] == shislo[2] != shislo[0]:
    print("да")    
else: 
    print("нет")
