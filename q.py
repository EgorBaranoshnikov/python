fin  = open("input.txt")
strings = fin.readlines()
s = strings[1].split(' ')
q = range(len(s))
f = strings[0]
d = int(f)
arr = []
for i in q:
   t = d - 1 - i
   arr.insert(i, s[t])
print(*arr, sep=" ")