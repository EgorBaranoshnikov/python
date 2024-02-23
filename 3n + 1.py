n = 295147905179361670568
q = n
def a(q):
    while q != 1:
        if q % 2 == 0:
            q = q / 2
        else:
            q = q * 3 + 1
while True:
    a(q)
    n += 1
    q = n
    print(n)                            