a = []
def pereklad ( n, start, fin, a):
    if n <= 0:
      return
    vrem = 6 - start - fin
    pereklad(n-1, start, vrem, a)
    a.append(1)
    print(n, start, fin)
    pereklad(n-1, vrem, fin, a)
pereklad(60, 1, 3, a)
print(len(a))