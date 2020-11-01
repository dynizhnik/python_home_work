from ua.univer.lesson02.figures.figure import *

def main():
    print("1. прямоугольник")
    print("2. прямоугольный треугольник")
    print("3. равносторонний треугольник")
    print("4. ромб")
    answer = int(input("Enter task: "))
    if answer == 1:
        print_rectangle(0,20)
    elif answer == 2:
        print_right_triangle()
    elif answer == 3:
        print_equilateral_triangle()
    elif answer == 4:
        print_rhombus()


if __name__ == '__main__':
    main()
