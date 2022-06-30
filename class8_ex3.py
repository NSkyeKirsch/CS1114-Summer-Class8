import math
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "X:{}  Y:{}".format(self.x, self.y)

    def get_coordinates(self):  # Accessor - returns a tuple of the coordinates for my shape
        return self.x, self.y


class Rectangle(Shape):  # Child class
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1)  # call parent initializer, send x1 and y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return "X:{}  Y:{}    X2:{}  Y2:{}".format(self.x, self.y, self.x2, self.y2)

    def calc_area(self):
        return math.fabs(self.x - self.x2) * math.fabs(self.y - self.y2)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return super().__str__() + "   radius {:3.2f}".format(self.radius)

    def calc_area(self):
        return math.pi * self.radius ** 2


class Square(Rectangle):
    def __init__(self, x, y, width, length):
        if width == length:
            super().__init__(x, y, x+length, y+length)


def main():
    my_shape = Shape(5, 10)
    print(my_shape, my_shape.get_coordinates())

    my_rect = Rectangle(3, 3, 12, 9)
    print(my_rect, ',', my_rect.calc_area())

    my_circ = Circle(12.456, 12, 0)
    print("Circle: ", my_circ, my_circ.calc_area())


if __name__ == "__main__":
    main()
