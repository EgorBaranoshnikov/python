# 1

fin  = open("input.txt")
strings = fin.readlines()
mas = strings[1].split()
kol = int(strings[0])
ind = -1
pro = 0
numOfMost = 0

# 2

for i in range(kol):
    ind += 1
    if int(mas[ind]) <= 437:
      numOfMost = i + 1
      break


# 3

if numOfMost == 0: 
   print("No crash")
else:
   print("Crash", numOfMost)