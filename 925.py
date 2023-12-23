fin  = open("input.txt")
strings = fin.readlines()
min = 0
max = 0
pr = 0
pr1 = 0
strings1 = strings[0].split()
strings2 = strings[1].split()
strx = int(strings2[0])
str3 = int(strings2[1])
str4 = int(strings2[2])
str5 = int(strings2[3])
str1 = int(strings1[0])
if str1 == 2:
  min = str3
  if str4 < min:
    min = str4
  if str5 < min:
    min = str5
  strx
  print(min)
if str1 == 1:
  x1 = strx - str5
  x2 = strx - str4
  x = x1 + x2
  otv = str3 - x 
  if otv < 0:
    otv = 0
  print(otv)
