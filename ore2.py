fin  = open("input.txt")
strings = fin.readlines()
mas = int(strings[0])
ind = 1
max = 0
prov = 0


for i in range(mas):
   tek = strings[ind]
   tek1 = tek.split()
   if int(tek1[0]) > int(tek1[1]):
      max += int(tek1[0])
   else:
      max += int(tek1[1])
   ind += 1

if max % 3 == 0:
   ind = 1
   a = 1
   for i in range(10000):
      for i in range(mas):
        tek = strings[ind]
        tek1 = tek.split()
        if int(tek1[0]) + a == int(tek1[1]) or int(tek1[1]) + a == int(tek1[0]):
            print(tek)
            print(max - a)
            prov += 1
            break
        ind += 1
      if prov > 0:
         break
      else:
         a += 1
         if a % 3 == 0:
            a += 1
         ind = 1


else:
   print(max)