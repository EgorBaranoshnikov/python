fin  = open("input.txt")
strings = fin.readlines()
nom = int(strings[0])
min = nom * 5

otv_sha = int(min / 60)
sha = otv_sha * 60
otv_min = (min - sha)

if otv_min == -5:
    otv_sha -= 1
    otv_min = 55
if nom > 146:
    print("NO")
else:
    print(int(otv_sha), int(otv_min))