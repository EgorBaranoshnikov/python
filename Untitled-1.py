if e < f:
   print("2")
if e > f:
   print("1")
if e == f:
   print("DRAW")
if g < h:
   print("2")
if g > h:
   print("1")
if g == h:
   print("DRAW")
if i < k:
   print("2")
if i > k:
   print("1")
if i == k:
   print("DRAW")
if l < m:
   print("2")
if l > m:
   print("1")
if l == m:
   print("DRAW")


count = 0
qqq = input("")
for zzz in qqq:
    if zzz == "2":
        count += 1
print("count:", count)


if e < f:
   k2 += 1
if e > f:
   k1 += 1
if e == f:
    k2 += 0
if g < h:
    k2 += 1
if g > h:
    k1 += 1
if g == h:
    k2 += 0
if i < k:
    k2 += 1
if i > k:
    k1 += 1
if i == k:
    k2 += 0
if l < m:
    k2 += 1
if l > m:
    k1 += 1
if l == m:
    k2 += 0

if k1 < k2:
   print("2")
if k1 > k2:
    print("1")
if k1 == k2:
   print("DRAW")