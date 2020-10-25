import turtle
R = 60

A_X = -150
A_Y = 25

B_X = -75
B_Y = -25

C_X = 0
C_Y = 25

D_X = 75
D_Y = -25

E_X = 150
E_Y = 25

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(A_X,A_Y)
turtle.pendown()
turtle.circle(R)
turtle.penup()
turtle.goto(B_X,B_Y)
turtle.pendown()
turtle.circle(R)
turtle.penup()
turtle.goto(C_X,C_Y)
turtle.pendown()
turtle.circle(R)
turtle.penup()
turtle.goto(D_X,D_Y)
turtle.pendown()
turtle.circle(R)
turtle.penup()
turtle.goto(E_X,E_Y)
turtle.pendown()
turtle.circle(R)
turtle.done()