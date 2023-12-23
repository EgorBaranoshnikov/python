fin  = open("input.txt")
strings = fin.readlines()
a = int(strings[0])
if a == 1 or a == 2 or a == 12:
   print("Winter")
elif a >= 3 and a <= 5:
   print("Spring")
elif a >= 6 and a <= 8:
   print("Summer")
elif a >= 9 and a <= 11:
   print("Autumn")
else:
   print("Error")