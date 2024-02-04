a = ["H", "H", "B"]
for i in range(20):
    a.append('H')
    p = 2
    for i in range((len(a) - 1) * 2 + 1 - len(a)):
        if a[len(a) - p] == "B":
            a.append('H')
            p += 2
        elif a[len(a) - p] == "H":
            a.append('B')
            p += 2

import turtle
turtle.shape("turtle")
size = 10
indi = 0
#turtle.left(90)
turtle.forward(size)
for i in range(len(a)):
    if a[indi] == "H":
        turtle.left(90)
        turtle.forward(size)
        indi += 1
    if a[indi] == "B":
        turtle.right(90)
        turtle.forward(size)
        indi += 1
