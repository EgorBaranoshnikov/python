fin  = open("input.txt")
strings = fin.readlines()
numbers = strings[1].split()
ind = 0
ind1 = 1
ind2 = 0
b  = []
o1 = []
o2 = []
otv = 0
nit = 0
pr = 0
pr1 = 0
pr2 = 1
for q in range(len(numbers)):
   a = int(numbers[ind])
   b.append(a)
   ind += 1
b.sort()


ot0 = b[1] - b[0]
ot1 = b[len(numbers) - 1] - b[len(numbers) - 2]
for i in range(len(numbers) - 2):
   ott1 = b[ind1] - b[ind1 - 1]
   ott2 = b[ind1 + 1] - b[ind1]
   ind1 += 1
   o1.append(ott1)
   o2.append(ott2)


for w in range(len(numbers) - 2):
   if o1[ind2] > o2[ind2]:
      otv += o2[ind2]
      pr = 1
   if pr == 0:
      otv += o1[ind2]
      if pr1 == 0:
         ot0 = 0
         pr1 += 1
      if pr2 == len(o1) - 1:
         ot1 = 0
   pr2 += 1
   ind2 += 1
   pr = 0
   


otv += ot0 + ot1
print(otv)


