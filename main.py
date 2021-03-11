import Circle
import Square

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
