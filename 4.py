fin  = open("input.txt")
strings = fin.readlines()
ч1 = int(strings[0])
ч1з = ч1 * 100
ч3 = 9 - ч1
ответ = ч1з + 90 + ч3
print(ответ)