fin = open("input.txt")
strings = fin.readlines()
or0 = strings[0].split()
ot = int(or0[0])
do = int(or0[1])
otv = do - ot
if otv > 12:
   otv1 = otv - 12
if otv < 0:
   otv1 = 12 - ot + do
if otv > 0 and otv < 12:
   otv1 = otv
print(otv1)