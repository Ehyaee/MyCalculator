import Rectangle

print("Welcom\n What do you want to make?")
print("1)Circle\n2)Square\n3)Rectangle\n4)Triangle")
shap = int(input())

if shap == 3:
    side1 = int(input())
    side2 = int(input())
    my_rect = Rectangle.Rectangle(side1,side2)
    print("Rectangle area = ",my_rect.getArea())
    print("Rectangle perimeter = ",my_rect.getPerimeter())