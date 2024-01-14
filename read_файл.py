def sum(a, b):    
    c = a + b
    d = a - b
    return c, d

def str2():
    fin  = open("input.txt")
    strings = fin.readlines()
    q = strings[0]
    w = strings[1]
    return q, w