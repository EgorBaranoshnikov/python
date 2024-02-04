fin  = open("input.txt")
strings = fin.readlines()
hh_ot = int(strings[0][0]) * 10 + int(strings[0][1])
mm_ot = int(strings[0][3]) * 10 + int(strings[0][4])
mas = strings[1].split()
hh_po = int(mas[0])
mm_po = int(mas[1])

hh_pr = hh_ot + hh_po
if hh_pr >= 24:
    hh_pr = hh_pr % 24


mm_pr = mm_ot + mm_po
if mm_pr >= 60:
    hh_pr += int(mm_pr / 60)
    mm_pr = mm_pr % 60

if hh_pr >= 24:
   hh_pr -= 24

if mm_pr >= 10 and hh_pr < 10:
   result = "0" + str(hh_pr) + ":" + str(mm_pr)
if mm_pr < 10 and hh_pr >= 10:
   result = str(hh_pr) + ":" + "0" + str(mm_pr)
if mm_pr < 10 and hh_pr < 10:
   result = "0" + str(hh_pr) + ":" + "0" + str(mm_pr)
if mm_pr >= 10 and hh_pr >= 10:
   result = str(hh_pr) + ":" + str(mm_pr)

print(result)