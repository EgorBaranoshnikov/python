fin  = open("input.txt")
strings = fin.readlines()
stringsx = strings[0].split(' ')
ind = range(len(stringsx))
otx = 0
a = 0
for i in ind:
   si = stringsx[i]
   six = int(si)
   if six > 727:
     a += 2
   if six < 94:
     a += 2
   if six >= 94 and six <= 727:
      if otx > six:
         otx = otx
      if otx < six:
         otx = six
if a > 1:
   print("Error")
if a < 1:
   print(otx)