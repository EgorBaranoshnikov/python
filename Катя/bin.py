for i in range(1000):
    d=bin(i)[2:]
    if i % 2 == 0:
        d = "1" + d + "0"
    else:
        d = "11" + d + "11"
    des = int(d, 2)
    if des > 52:
        print(i)
        break