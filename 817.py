fin  = open("input.txt")
strings = fin.readlines()
mas = strings[0].split()
x_lin = int(mas[0]) 
y_lin = int(mas[1])
hsir = int(mas[2])
dlin = int(mas[3])

kol_per = x_lin * y_lin
kol_l = x_lin + y_lin
per_1 = hsir * hsir
per_vse = per_1 * kol_per
S_lin_1 = hsir * dlin
S_lin_vse = S_lin_1 * kol_l
otv = S_lin_vse - per_vse
print(otv)