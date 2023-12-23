fin  = open("input.txt")

 
strings = fin.readlines()

k1 = 0
k2 = 0


for str in strings:
   a = str.split()
   o1 = int(a[0])
   o2 = int(a[1])
   k1 += o1
   k2 += o2



if k1 < k2:
   print("2")
if k1 > k2:
    print("1")
if k1 == k2:
   print("DRAW")