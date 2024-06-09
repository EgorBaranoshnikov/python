fin  = open("input.txt")
strings = fin.readlines()
nom = int(strings[0])

#for nom in range(250):

otv_min = 0
otv_sha = 0
if nom % 2 != 0:
    nom += 1
    otv_min -= 10
elif nom % 2 == 0:
    otv_min -= 5


nom_1 = nom / 2
nom_2 = nom_1 * 10
nom_2 = nom_2 + otv_min

otv_sha = int(nom_2 / 60)
sha = otv_sha * 60
otv_min = nom_2 - sha

if otv_min == -5:
    otv_sha -= 1
    otv_min = 55
if int(strings[0]) >= 146:
    print("NO")
else:
    print(int(otv_sha), int(otv_min))