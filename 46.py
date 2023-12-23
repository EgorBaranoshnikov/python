fin  = open("input.txt")
strings = fin.readlines()
stringsx = int(strings[0])
strq = ""

ind = 0
x = "2.7182818284590452353602875"
for i in range(stringsx + 2):
   if stringsx == 0:
      break
   if stringsx == 25:
      break

   strq = strq + x[ind]
   ind += 1
   if ind == stringsx + 2:
      w = int(x[stringsx + 2])
      if w >= 5:
         b = int(x[stringsx + 2])
         b = str(b)
         strq = strq[:-1] + b
for i in range(1):
   if stringsx == 0:
      print(3)
      break
   if stringsx == 25:
      print(2.7182818284590452353602875)
      break
   print(strq)