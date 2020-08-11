import turtle

def perfecttriangle(t, size):
    for i in range(3):
        t.forward(size)
        t.right(120)

def circle1(t,sides,distance):
    for i in range (sides):
        t.forward(distance)
        t.left(360/sides)
def circle2(t,sides,distance):
    for i in range (sides):
        t.forward(distance)
        t.right(360/sides)

def monster1(t,sides,distance):
    for i in range (100):
        t.forward(distance + 0.2*i)
        t.right(90/sides)

def monster2(t,sides,distance):
    for i in range (100):
        t.forward(distance + 0.2*i)
        t.left(90/sides)

kevin = turtle.Turtle()

kevin.shape('turtle')
kevin.speed('fastest')
kevin.color('green')

circle2(kevin,50,10)



turtle.mainloop()
