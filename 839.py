fin  = open("input.txt")
tek = fin.readlines()
ind= 0
a = 0
for i in range(len(tek[0])):
   if tek[0][ind] == "0":
      a += 1
      print("NO")
      break
   ind += 1
if a == 0:
   print("YES")