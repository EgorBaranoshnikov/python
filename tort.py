import turtle
turtle.shape("turtle")
size = 500000
n = 10
def koh(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        koh(size / 3, n - 1)
        #turtle.left(60)
        turtle.left(90)
        koh(size / 3, n - 1)
        #turtle.right(120)
        turtle.right(180)
        koh(size / 3, n - 1)
        #turtle.left(60)
        turtle.left(90)
        koh(size / 3, n - 1)
koh(size, n)