def test():
    p1 = 1
    p2 = 0
    p3 = 0
    for q in range(10):        
        for q in range(p1 + 1):
            p1 += 1
            p2 = p1 + 1
            for w in range(p1):
                p2 = p2 - 1
                p3 = p1 + 1
                for w in range(p1):  
                    p3 = p3 - 1
                    print(p1, p2, p3)
test()