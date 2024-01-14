from graph import *
def quadro(x1, y1, x2, y2, level):
    if level < 1:
       return
    rectangle(x1, y1, x2, y2)

    x1 = ((y2 - y1) / 3 + y1) - ((y2 - y1) / 6)
    x2 = ((y2 - y1) / 3 * 2 + y1) + ((y2 - y1) / 6)
    y1 = ((y2 - y1) / 3 + y1)
    y2 = ((y2 - y1) / 3 * 2 + y1)
    
    quadro(x1, y1, x2, y2, level - 1)
    #quadro( level - 1)
    #quadro( level - 1)
    #quadro( level - 1)
quadro(100, 100, 200, 200, 10)
run()
