fin  = open("input.txt")
strings = fin.readlines()
a = strings[0].split()
o0 = int(a[0])
o1 = int(a[1])
o2 = int(a[2])
q = o0 + o1
w = q - o2
if w < 0:
   print("Impossible")
if w >= 0:
   print(w)