fin  = open("input.txt")
strings = fin.readlines()
mas = strings[1].split()
p1 = int(strings[0])
ind = 0
sh = []
nsh = []
indi = 0

for i in range(p1):
   p = int(mas[ind])
   if p % 2 == 0:
      sh.append(p)
   else:
      nsh.append(p)
   ind += 1

print(*nsh, sep=" ")
print(*sh, sep=" ")
if len(sh) >= len(nsh):
   print("YES")
else:
   print("NO")