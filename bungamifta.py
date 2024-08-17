import turtle

def draw_flower():
    # Atur kecepatan turtle
    turtle.speed(3)

    # Posisi awal
    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
    turtle.pendown()
    turtle.right(90)

    # Dasar bunga
    turtle.fillcolor("#d19aec")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.forward(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.forward(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.forward(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.forward(45)
    turtle.right(165)
    turtle.forward(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()

    # Kelopak 1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)

    # Kelopak 2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)

    # Daun 1
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(45)
    turtle.fillcolor("#caafd7")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()

    turtle.right(135)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(85)
    turtle.left(90)
    turtle.forward(80)

    # Daun 2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("#caafd7")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()

    turtle.left(135)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(200, 60)

    turtle.done()

# Panggil fungsi untuk menggambar bunga
draw_flower()
