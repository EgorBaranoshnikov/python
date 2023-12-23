def sp1(mas):
    kol = int(mas[0])
    st = int(mas[1])
    fn = int(mas[2])
    stp = st
    stm = st
    if st == kol:
        stp = 0
    for i in range(kol):
        stp += 1
        stm -= 1
        if stm == 0:
            stm = kol
        if stp == kol:
            stp = 0
        if stm == fn:
            return i
            break
        if stp == fn:
            return i
            break


def sp2(mas):
    kol = int(mas[0])
    st = int(mas[1])
    fn = int(mas[2])
    if st < fn:
        v1 = fn - st - 1
        v2 = kol - fn + st - 1
    else:
        v1 = st - fn - 1
        v2 = kol - st + fn - 1

    if v1 < v2:
        return v1
    else:
        return v2


def test():
    p1 = 1
    p2 = 0
    p3 = 0
    for q in range(100):        
        for q in range(p1 + 1):
            p1 += 1
            p2 = p1 + 1
            for w in range(p1):
                p2 = p2 - 1
                p3 = p1 + 1
                for w in range(p1):
                   
                    p3 = p3 - 1
                    if p1 > 100:
                        return
                    if p2 == p3:
                        continue
                    mas = [p1, p2, p3]

                    otvet1 = sp1(mas)
                    otvet2 = sp2(mas)

                    if otvet1 != otvet2:
                        print(mas)
                        


                    
test()