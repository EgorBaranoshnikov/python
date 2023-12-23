fin  = open("input.txt")
strings = fin.readlines()
numbers = strings[1].split()
ind = 0
b  = []
for q in range(len(numbers)):
   a = int(numbers[ind])
   b.append(a)
   ind += 1


b.sort()
#for i in range(len(b) - 1):
#    for q in range(len(b) - 1):
#        if b[q] > b[q + 1]:
#            b[q], b[q + 1] = b[q + 1], b[q]
print(*b)