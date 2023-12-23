fin  = open("input.txt")
strings = fin.readlines()
ms = []
ms1 = []
pars = []
pr = 0
pro = 0
prove = 0
ind = 1
ma = 0
otv1 = 0
otv2 = 0
for q in strings:
    str = q.rstrip()
    b = str[(len(str) - 1)]
    pr += 1
    if b == "3":
      str = int(str)
      ms.append(str)
      if pr == 1:
         c = ind + 1
         prv1 = strings[c - 1].rstrip()
         prv = prv1[(len(prv1) - 1)]
         if prv != "3":
            pars.append([int(strings[ind -1].rstrip()), int(strings[c -1].rstrip())])      
      if pr == len(strings):         
         c = ind - 1 
         prv1 = strings[c - 1].rstrip()
         prv = prv1[(len(prv1) - 1)]
         if prv != "3": 
            pars.append([int(strings[ind -1].rstrip()), int(strings[c -1].rstrip())])    
      if pr > 1 and pr < len(strings):
         c = ind + 1
         prv1 = strings[c - 1].rstrip()
         prv = prv1[(len(prv1) - 1)]
         if prv != "3":
            pars.append([int(strings[ind -1].rstrip()), int(strings[c -1].rstrip())])    
         c = ind - 1
         prv1 = strings[c - 1].rstrip()
         prv = prv1[(len(prv1) - 1)]
         if prv != "3":
            pars.append([int(strings[ind -1].rstrip()), int(strings[c -1].rstrip())])    
    else:
       str = int(str)
       ms1.append(str)
    ind += 1
for e in range(len(ms)):
      if pro == 0:
         ma = int(ms[e])
      if pro > 0:
         if ma < int(ms[e]):
            ma = int(ms[e])
      pro += 1
max = ma ** 2
for i in range(len(pars)):
   ko = pars[i][0] ** 2 + pars[i][1] ** 2
   if ko > max:
      otv1 += 1
      if prove == 0:
         otv2 = ko
      if otv2 < ko:
         otv2 = ko
      prove += 1
print(otv1)
print(otv2)