from graph import *
def quadro(xCen, yCen, r, level):
    if level < 1:
       return
    circle(xCen, yCen, r)
    nextR = r // 2
    quadro(xCen - r, yCen, nextR, level - 1)
    quadro(xCen + r, yCen, nextR, level - 1)
    quadro(xCen, yCen - r, nextR, level - 1)
    quadro(xCen, yCen + r, nextR, level - 1)
quadro(300, 300, 50, 3)
run()
