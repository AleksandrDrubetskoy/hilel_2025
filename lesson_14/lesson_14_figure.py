from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, name, **kwargs):
        self.name = name

    @abstractmethod
    def figure_area(self, **kwargs):
        pass

    @abstractmethod
    def figure_perimeter(self, **kwargs):
        pass

    def __str__(self):
        return f"The {self.name} has perimeter {self.figure_perimeter()} and area {self.figure_area()}"


class Square(Figure):

    def __init__(self, name, is_square: bool, side):
        super().__init__(name=name)
        self.is_square = is_square
        self.side = side

    def figure_area(self):
        if self.is_square:
            return self.side ** 2

    def figure_perimeter(self):
        if self.is_square:
            return self.side * 4


class Rectangle(Figure):

    def __init__(self, name, is_rectangle: bool, side_a, side_b):
        super().__init__(name=name)
        self.is_rectangle = is_rectangle
        self.side_a = side_a
        self.side_b = side_b

    def figure_area(self):
        if self.is_rectangle:
            return self.side_a * self.side_b

    def figure_perimeter(self):
        if self.is_rectangle:
            return (self.side_a + self.side_b) * 2


class Triangle(Figure):

    def __init__(self, name, is_triangle: bool, side_a, side_b, base):
        super().__init__(name=name)
        self.is_triangle = is_triangle
        self.side_a = side_a
        self.side_b = side_b
        self.base = base
        half_perimeter = (self.side_a + self.side_b + self.base) / 2
        some_math = (half_perimeter * (half_perimeter - self.base) *
                     (half_perimeter - self.side_a) * (half_perimeter - self.side_b)) ** 0.5
        self.height = 2 / self.base * some_math

    def figure_area(self):
        if self.is_triangle:
            return self.base * self.height / 2

    def figure_perimeter(self):
        if self.is_triangle:
            return self.side_a + self.side_b + self.base


square_1 = Square("square", True, 5)
print(square_1)
print("_" * 44)
rectangle_1 = Rectangle("rectangle", True, 5, 8)
print(rectangle_1)
print("_" * 44)
triangle_1 = Triangle("triangle", True, 10, 10, 8)
print(triangle_1)
print("_" * 44)
