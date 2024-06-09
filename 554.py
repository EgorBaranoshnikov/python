fin  = open("input.txt")
strings = fin.readlines()
f = 1
tek = strings[0].split()
tek1 = int(tek[0])
for i in range(tek1):
   f = f + (i + 1)
print(f)