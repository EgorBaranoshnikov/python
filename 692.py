fin  = open("input.txt")
strings = fin.readlines()
bin = int(strings[0])
a = bin 
while a > 1:
   a = a / 2
if a == 1:
   print("YES")
else: 
   print("NO")