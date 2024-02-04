fin  = open("input.txt")
strings = fin.readlines()
mas1 = strings[0].split()
mas2 = strings[1].split()
p11 = int(mas1[0])
p12 = int(mas1[1])
p13 = int(mas1[2])

p21 = int(mas2[0])
p22 = int(mas2[1])
p23 = int(mas2[2])


pot1 = p11 / 100 * (100 - p12)
pot2 = p21 / 100 * (100 - p22)
if pot1 > pot2:
    pot1 = pot1 - (pot1 - pot2)
if pot2 > pot1:
    pot2 = pot2 - (pot2 - pot1)
oct1 = p11 - pot1
oct2 = p21 - pot2

ryb1 = oct1 * p13
ryb2 = oct2 * p23



otv = ryb1 + ryb2
otv = int(otv)
print(otv)