fin  = open("input.txt")
strings = fin.readlines()
a = int(strings[0]) 
otv = a * a - (a + (a-1) * 2)
print(otv)