fin  = open("input.txt")
strings = fin.readlines()
stringsx = int(strings[0])
strq = ""

ind = 0
x = "2.7182818284590452353602875"


for i in range(stringsx + 2):
   strq += x[ind]
   ind += 1


if stringsx == 0:
   print("3")
elif stringsx == 25:
   print("2.7182818284590452353602875")
else:
   # Взять следующее число
   posledneeChislo = int(x[ind])
   # Если оно больше 4 то последнее число увеличить на 1
   if posledneeChislo >= 5:
      posl = str(int(strq[ind-1]) + 1)
      strq = strq[:-1]
      strq += posl
   print(strq)