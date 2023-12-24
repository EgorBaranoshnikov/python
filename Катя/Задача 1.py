
ras_km1 = float(input("Введите расстояние в километрах: "))
ras_ft1 = float(input("Введите расстояние в футах: "))

ras_km2 = round(ras_ft1 * 0.305 / 1000)
if ras_km1 < ras_km2:
    print("В километрах меньше")
if ras_km2 < ras_km1:
    print("В футах меньше")
if ras_km2 == ras_km1:
    print("Они равны")