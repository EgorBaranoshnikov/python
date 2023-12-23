fin = open("input.txt")
strings = fin.readlines()
elements = strings[0].split()

maxIndex = -1
minIndex = -1

for index in range(len(elements)):

   num = int(elements[index])
   ostatok = (index + 1) % 2
   if ostatok == 0:
      if maxIndex == -1:
         maxIndex = index
      if maxIndex > -1 and num > int(elements[maxIndex]):
         maxIndex = index
   else:
      if minIndex == -1:
         minIndex = index
      if minIndex > -1 and num < int(elements[minIndex]):
         minIndex = index

sum = 0
if (maxIndex > -1):
   sum = sum + int(elements[maxIndex])
if (minIndex > -1):
   sum = sum + int(elements[minIndex])

print(sum)