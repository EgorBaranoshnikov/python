fin  = open("input.txt")
strings = fin.readlines()
n = int(strings[0])
otv = 0
for i in range(n // 2):
   if n % (i + 1) == 0:
      otv += i + 1
otv = otv + n
print(otv)