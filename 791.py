fin  = open("input.txt")
strings = fin.readlines()
p1 = int(strings[0])
sh1 = p1 - 1
sh2 = p1 + 1
sh3 = p1 + 16
sh4 = p1 - 16

otv = [sh1, sh2, sh3, sh4]
#otv.sort()
if otv[0] == 0 or otv[0] == 7 or otv[0] == 15 or otv[0] == 23 or otv[0] == 31 or otv[0] == 39 or otv[0] == 47 or otv[0] == 55 or otv[0] == 63:
   otv = otv[:-1]
if otv[1] == 9 or otv[1] == 17 or otv[1] == 25 or otv[1] == 32 or otv[1] == 41 or otv[1] == 49 or otv[1] == 57 or otv[1] == 65:
   otv = otv.remove(sh2)
print(otv)