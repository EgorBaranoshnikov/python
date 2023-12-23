fin  = open("input.txt")
strings = fin.readlines()
k0 = 0
t = 0
for q in strings[0]:
   if (q == "\n"):
      continue
   a = int(q)
   if a == 0:
      k0 += 1
   if a == 1:
      e = k0
      if e > 0 and k0 == e:
         k0 = 0
         if t > e:
            t += 0
         if t < e:
            t = e
         if t == e:
            t += 0
print(t)