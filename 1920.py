fin  = open("input.txt")
strings = fin.readlines()
lin = int(strings[0]) 
kryg = int(strings[1])
chas_1 = lin * 2
chas_vce = (kryg + 1) * chas_1
if lin == 0:
   print(kryg + 1)
elif kryg == 0:
   print(lin * 2)
elif lin == 0 and kryg == 0:
   print(1)
elif lin > 0 and kryg > 0:
   print(chas_vce)