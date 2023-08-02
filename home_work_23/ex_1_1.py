"""
Folosind clasele Shape, Circle, Rectangle și Square.
Implementați metodele necesare pentru:
• Obțineți aria formei (Circle, Rectangle, Square), ca proprietate. Cu excepția formei de bază (Shape, care nu poate
   avea o arie).
• Să puteți compara forme (doar forme de același tip pot fi comparate)
   • Numai forme de același tip pot fi comparate:
       • Trebuie să pot compara un cerc cu un alt cerc.
       • Nu trebuie să pot compara un cerc cu un pătrat.
   • Trebuie să pot compara un pătrat și un dreptunghi, deoarece au aceleași proprietăți.
   • La compararea dreptunghiurilor, comparați aria dreptunghiului (nu lățimea și lungimea).
• Să puteți efectua operații de adunare, scădere și înmulțire a formelor (de exemplu, rectangle1 + rectangle2).
   • Când efectuați astfel de operații, efectuați operațiile pe proprietățile comune ale celor 2 obiecte (
       lățime/lungime/radius).
   • La efectuarea scăderii, valoarea proprietăților unei forme nu trebuie să fie mai mică decât 0.
   • Numai formele cu aceleași proprietăți pot avea operațiile efectuate (ex: Cerc și Pătrat nu pot fi adăugate,
       Pătrat și Dreptunghi pot fi adăugate). Puteți folosi verificări cu isinstance și issubclass pentru a efectua
       aceste verificări.
   • La efectuarea înmulțirii, permiteți și înmulțirea obiectului cu un număr.
       • Exemplu: Rectangle(2,4) * 2 = Rectangle(4,8)
"""
# Solutie

import math


class Shape:
    def __init__(self, inner_color, border_color):
        self._inner_color = inner_color
        self._border_color = border_color

    def get_inner_color(self):
        return self._inner_color

    def set_inner_color(self, color):
        self._inner_color = color

    def get_border_color(self):
        return self._border_color

    def set_border_color(self, color):
        self._border_color = color


class Circle(Shape):
    def __init__(self, inner_color, border_color, radius):
        super().__init__(inner_color, border_color)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    @property
    def area(self):
        return math.pi * self._radius ** 2

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self._inner_color, self._border_color, self._radius + other._radius)
        raise ValueError("Shapes of different types cannot be added.")

    def __sub__(self, other):
        if isinstance(other, Circle):
            new_radius = self._radius - other._radius
            if new_radius >= 0:
                return Circle(self._inner_color, self._border_color, new_radius)
            else:
                raise ValueError("Shape properties cannot be less than 0.")
        raise ValueError("Shapes of different types cannot be subtracted.")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Circle(self._inner_color, self._border_color, self._radius * factor)
        raise ValueError("Invalid multiplication factor.")


class Rectangle(Shape):
    def __init__(self, inner_color, border_color, width, length):
        super().__init__(inner_color, border_color)
        self._width = width
        self._length = length

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    @property
    def area(self):
        return self._width * self._length

    def __add__(self, other):
        if isinstance(other, (Rectangle, Square)):
            return Rectangle(self._inner_color, self._border_color, self._width + other._width,
                             self._length + other._length)
        raise ValueError("Shapes of different types cannot be added.")

    def __sub__(self, other):
        if isinstance(other, (Rectangle, Square)):
            new_width = self._width - other._width
            new_length = self._length - other._length
            if new_width >= 0 and new_length >= 0:
                return Rectangle(self._inner_color, self._border_color, new_width, new_length)
            else:
                raise ValueError("Shape properties cannot be less than 0.")
        raise ValueError("Shapes of different types cannot be subtracted.")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Rectangle(self._inner_color, self._border_color, self._width * factor, self._length * factor)
        raise ValueError("Invalid multiplication factor.")


class Square(Rectangle):
    def __init__(self, inner_color, border_color, side_length):
        super().__init__(inner_color, border_color, side_length, side_length)

    def __add__(self, other):
        if isinstance(other, (Rectangle, Square)):
            return Square(self._inner_color, self._border_color, self._width + other._width)
        raise ValueError("Shapes of different types cannot be added.")

    def __sub__(self, other):
        if isinstance(other, (Rectangle, Square)):
            new_width = self._width - other._width
            if new_width >= 0:
                return Square(self._inner_color, self._border_color, new_width)
            else:
                raise ValueError("Shape properties cannot be less than 0.")
        raise ValueError("Shapes of different types cannot be subtracted.")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Square(self._inner_color, self._border_color, self._width * factor)
        raise ValueError("Invalid multiplication factor.")


# Verificare

circle1 = Circle("red", "black", 5)
circle2 = Circle("blue", "white", 3)

print("Circle 1 area:", circle1.area)
print("Circle 2 area:", circle2.area)
print("Circle 1 + Circle 2:", (circle1 + circle2).area)
print("Circle 1 - Circle 2:", (circle1 - circle2).area)
print("Circle 1 * 2:", (circle1 * 2).area)

rectangle1 = Rectangle("green", "gray", 4, 6)
rectangle2 = Rectangle("yellow", "orange", 2, 3)

print("Rectangle 1 area:", rectangle1.area)
print("Rectangle 2 area:", rectangle2.area)
print("Rectangle 1 + Rectangle 2:", (rectangle1 + rectangle2).area)
print("Rectangle 1 - Rectangle 2:", (rectangle1 - rectangle2).area)
print("Rectangle 1 * 1.5:", (rectangle1 * 1.5).area)

square1 = Square("purple", "pink", 4)
square2 = Square("cyan", "magenta", 2)

print("Square 1 area:", square1.area)
print("Square 2 area:", square2.area)
print("Square 1 + Square 2:", (square1 + square2).area)
print("Square 1 - Square 2:", (square1 - square2).area)
print("Square 1 * 3:", (square1 * 3).area)
