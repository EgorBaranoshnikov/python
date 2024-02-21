n = 3
q = n

def a(q):
    while q != 1:
        if q % 2 == 0:
            q = q / 2
        else:
            q = q * 3 + 1
n += 1
q = n
print(n)
for i in range(10):
    a(q)
    n += 1
    q = n
    print(n)