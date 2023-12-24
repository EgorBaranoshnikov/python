plosh_kryga = float(input("Введите площадь круга: "))
plosh_kvadr = float(input("Введите площадь квадрата: "))

diamt_kryga = 2 * ((plosh_kryga / 3.1415) ** (0.5)) 
storona_kvadr = plosh_kvadr ** (0.5)
gipatinuza_kvadr = ((storona_kvadr ** 2)*2) ** (0.5)

print("а) Круг")
if storona_kvadr >= diamt_kryga:
    print("Поместится в квадрате")
else:
    print("Не поместится в квадрате")


print("б) Квадрат")
if gipatinuza_kvadr <= diamt_kryga:
    print("Поместится в круге")
else:
    print("Не поместится в круге")