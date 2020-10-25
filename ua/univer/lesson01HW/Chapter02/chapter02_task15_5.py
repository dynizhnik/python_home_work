import turtle
R = 40

A_X = 100
A_Y =0

B_X = 0
B_Y = 100

C_X = 0
C_Y = -100

D_X = -100
D_Y = 0

turtle.hideturtle()
turtle.speed(0)
turtle.goto(0,-40)
turtle.circle(R)
turtle.penup()
turtle.goto(A_X,A_Y)
turtle.pendown()
turtle.write('East')
turtle.penup()
turtle.goto(B_X,B_Y)
turtle.pendown()
turtle.write('North')
turtle.goto(C_X,C_Y)
turtle.write('South')
turtle.penup()
turtle.goto(D_X,D_Y)
turtle.pendown()
turtle.write('West')
turtle.goto(A_X,A_Y)
turtle.done()