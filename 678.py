fin  = open("input.txt")
strings = fin.readlines()
ind = 0
tek = 1
for i in range(len(strings[0])):
   if strings[0][ind] == "A":
      if tek == 1:
         tek = 2
      elif tek == 2:
         tek = 1
   if strings[0][ind] == "B":
      if tek == 3:
         tek = 2
      elif tek == 2:
         tek = 3
   if strings[0][ind] == "C":
      if tek == 1:
         tek = 3
      elif tek == 3:
         tek = 1
   ind += 1
print(tek)