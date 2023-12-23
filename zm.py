zm = "a"
x1 = ": "
x2 = "       :"
print(x1, zm, x2)
dv = input("двигайся: ")
for i in dv:
   if i == "a":
      if x1 == ":":
         print("ты проиграл")
      if x1 == ": ":
         a1 = x1 = ":"
         a2 = x2 = ":       "
         print(a1, zm, a2)