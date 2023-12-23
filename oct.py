fin = open("input.txt")
strings = fin.readlines()
xuc = strings[0].split()
q = range(len(xuc))
ind = 0
k1 = 0
k2 = 0
ko1 = 0
ko2 = 0
cx1 = 0
cx2 = 0
for i in q:
   ot = int(xuc[ind])
   ind += 1
   otv = (i + 1) % 2
   if otv == 0:
      cx1 +=1
      k1 = ot
      if cx1 == 1:
         ko1 = k1
      if ko1 < k1:
         ko1 = k1
   if otv >= 1:
      cx2 +=1
      k2 = ot
      if cx2 == 1:
         ko2 = k2
      if ko2 > k2:
         ko2 = k2
   ot = 0
o = ko2 + ko1
print(o)