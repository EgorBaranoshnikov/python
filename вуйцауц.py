def d(a):
    if a == 1 or a == 2:
       return 1
    else:
       return d(a - 1) + d(a - 2) # рекурсия
print(d(50))