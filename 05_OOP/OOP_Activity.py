class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return self.length + self.width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(5, 6)
print(rectangle.perimeter())


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

square = Square(5)
print(square.perimeter())
print(square.area())







