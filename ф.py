fin  = open("input.txt")
strings = fin.readlines()
q = strings[0].split()
if (len(q)) == 1:
   ot = 1
   do = int(q[0])
if (len(q)) > 1:
   ot = int(q[0])
   do = int(q[1])
if do < 0:
   a = do * -1 + ot + 1
if do > 0:
   a = do - ot + 1
if do == 0:
   a = 0
b = ot + do
otv = b * a / 2
if a == -1:
   otv = 1
print(otv)