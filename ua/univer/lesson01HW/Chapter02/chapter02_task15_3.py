import turtle

A_X = 100
A_Y = 0

B_X = 0
B_Y = 100

C_X = -100
C_Y = 100

D_X = -100
D_Y = 0

E_X = 0
E_Y = -100

F_X = 100
F_Y = -100

turtle.hideturtle()
turtle.speed(0)
turtle.goto(A_X,A_Y)
turtle.goto(B_X,B_Y)
turtle.goto(C_X,C_Y)
turtle.goto(D_X,D_Y)
turtle.goto(E_X,E_Y)
turtle.goto(F_X,F_Y)
turtle.goto(C_X,C_Y)
turtle.penup()
turtle.goto(D_X,D_Y)
turtle.pendown()
turtle.goto(A_X,A_Y)
turtle.goto(F_X,F_Y)
turtle.penup()
turtle.goto(E_X,E_Y)
turtle.pendown()
turtle.goto(B_X,B_Y)
turtle.done()