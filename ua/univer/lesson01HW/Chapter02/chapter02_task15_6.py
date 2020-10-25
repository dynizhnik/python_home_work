import turtle

A_X = 90
A_Y = 90

B_X = 90
B_Y = -90

C_X = -90
C_Y = -90

D_X = -90
D_Y = 90

#Задаем пунктирные константы:
A_plus80_X = 80
A_plus40_X = 40
A_plus10_X = 10
A_minus10_X = -10
A_minus40_X = -40
A_minus80_X = -80

#Рисуем сплашной каркас:
turtle.hideturtle()
turtle.speed(0)
turtle.dot()
turtle.goto(A_X,A_Y)
turtle.dot()
turtle.goto(B_X,B_Y)
turtle.dot()
turtle.goto(D_X,D_Y)
turtle.dot()
turtle.goto(C_X,C_Y)
turtle.dot()
turtle.goto(A_X,A_Y)

#Рисуем верхнюю пунктирную линию:
turtle.goto(A_plus80_X,A_Y)
turtle.penup()
turtle.goto(A_plus40_X,A_Y)
turtle.down()
turtle.goto(A_plus10_X,A_Y)
turtle.penup()
turtle.goto(A_minus10_X,A_Y)
turtle.pendown()
turtle.goto(A_minus40_X,A_Y)
turtle.penup()
turtle.goto(A_minus80_X,A_Y)
turtle.pendown()
turtle.goto(D_X,D_Y)

#Рисуем нижнюю пунктирную линию:
turtle.penup()
turtle.goto(B_X,B_Y)
turtle.pendown()
turtle.goto(A_plus80_X,B_Y)
turtle.penup()
turtle.goto(A_plus40_X,B_Y)
turtle.down()
turtle.goto(A_plus10_X,B_Y)
turtle.penup()
turtle.goto(A_minus10_X,B_Y)
turtle.pendown()
turtle.goto(A_minus40_X,B_Y)
turtle.penup()
turtle.goto(A_minus80_X,B_Y)
turtle.pendown()
turtle.goto(C_X,C_Y)

turtle.done()