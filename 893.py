fin  = open("input.txt")
strings = fin.readlines()
a = int(strings[0])
if a == 1:
    print(1)
if a == 2:
    print(2)
if a > 2:
   otv = a * (a - 1) * (a - 2)
   print(otv)