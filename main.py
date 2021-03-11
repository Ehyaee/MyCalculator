
import Rectangle
import Circle
import Square
import Triangle

print("Welcom\n What do you want to make?")
print("1)Circle\n2)Square\n3)Rectangle\n4)Triangle")
shap = int(input())


if shap == 1:
    print("Enter the circle raduse:")
    r = int(input())
    circle = Circle.Circle(r)
    print("Circle with radius: ", r,
          "created\nwhat do you want to know about it?\n1)Area\n2)Perimeter")
    option = int(input())
    if option == 1:
        print(circle.getArea())
    elif option == 2:
        print(circle.getPerimeter())
        
elif shap == 2:
    print("Enter the square side length:")
    s = int(input())
    square = Square.Square(s)
    print("Square with side: ", s,
          "created\nwhat do you want to know about it?\n1)Area\n2)Perimeter")
    option = int(input())
    if option == 1:
        print(square.getArea())
    elif option == 2:
        print(square.getPerimeter())

        
elif shap == 3:
    print("Enter the rectangle sides length:")
    side1 = int(input())
    side2 = int(input())
    rectangular = Rectangle.Rectangle(side1,side2)
    print("what do you want to know about it?\n1)Area\n2)Perimeter")
    option = int(input())
    if option == 1:
        print(rectangular.getArea())
    elif option == 2:
        print(rectangular.getPerimeter())

elif shap == 4:
    print("Enter the triangle sides length:")
    print("base:\n")
    base = int(input())
    print("height:\n")
    height = int(input())
    print("b:\n")
    b = int(input())
    print("c:\n")
    c = int(input())
    triangle = Triangle.Triangle(base,height,b,c)
    print("what do you want to know about it?\n1)Area\n2)Perimeter")
    option = int(input())
    if option == 1:
        print(triangle.getArea())
    elif option == 2:
        print(triangle.getPerimeter())

